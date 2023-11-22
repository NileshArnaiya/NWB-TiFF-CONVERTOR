import argparse
from pynwb import NWBHDF5IO
from dandi.dandiapi import DandiAPIClient
import fsspec
from fsspec.implementations.cached import CachingFileSystem
import h5py
import pynapple as nap
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process NWB file from Dandi and convert to TIFF.')
    parser.add_argument('--dandiset_id', required=True, help='Dandiset ID')
    parser.add_argument('--file_path', required=True, help='Path to NWB file within the Dandiset')
    parser.add_argument('--cache_storage', default='nwb-cache', help='Cache storage directory')
    parser.add_argument('--output_path', default='output.tiff', help='Output TIFF file path')
    return parser.parse_args()

def main():
    args = parse_arguments()

    with DandiAPIClient() as client:
        asset = client.get_dandiset(args.dandiset_id, 'draft').get_asset_by_path(args.file_path)
        s3_url = asset.get_content_url(follow_redirects=1, strip_query=True)

    fs = CachingFileSystem(fs=fsspec.filesystem('http'), cache_storage=args.cache_storage)

    with h5py.File(fs.open(s3_url, 'rb')) as file:
        io = NWBHDF5IO(file=file, load_namespaces=True)

    print(io)

    custom_params = {"axes.spines.right": False, "axes.spines.top": False}
    sns.set_theme(style="ticks", palette="colorblind", font_scale=1.5, rc=custom_params)

    nwb = nap.NWBFile(io.read())
    print(nwb)

    use_key = ""
    for key, value in nwb.items():
        print(str(type(value)))
        if str(type(value)) == "<class 'pynapple.core.time_series.TsdFrame'>":
            print(f"{key} is a TsdFrame.")
            use_key = key

    print(use_key)
    data = nwb[use_key].values
    print(data.shape)

    imageio.imwrite(args.output_path, data)

if __name__ == "__main__":
    main()

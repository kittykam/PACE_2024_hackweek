import earthaccess
import xarray as xr
from xarray.backends.api import open_datatree
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from datetime import datetime, timezone
from random import randint
auth = earthaccess.login(persist=True)


# function: make sure dataset and flag have the same dimension on lat and lon

def Rrs_avg(dataset,flag, n):
    # dataset = 3D (not nested)
    # flag = 2D array flag
    # n = desired flag
    
    # add flag into the dataset
    dataset['flag'] = (('lat','lon'),flag)
    
    # pull lat lon index from flag
    lat_idx = np.where(flag == n)[0]
    lon_idx = np.where(flag == n)[1]
    
    # pull the Rrs from the selected location
    Rrs = dataset.Rrs.values[lat_idx, lon_idx,:]
    wv = dataset.wavelength

    # calculate mean and sd
    Rrs_mean = np.nanmean(Rrs,axis = 0)
    Rrs_sd = np.nanstd(Rrs, axis = 0)

    # return 
    return Rrs_mean, Rrs_sd

    #plot 
    fig, ax = plt.subplots(1)
    ax.plot(wv, Rrs_mean, lw=2, color='blue')
    ax.fill_between(wv, Rrs_mean+Rrs_sd, Rrs_mean-Rrs_sd, facecolor='blue', alpha=0.5)
    ax.set_title(r'Rrs spectral average : {} to {}'.format(datetime.fromisoformat(dataset.attrs['time_coverage_start'][:-1]).astimezone(timezone.utc).strftime("%Y-%m-%d"),
                                                           datetime.fromisoformat(dataset.attrs['time_coverage_end'][:-1]).astimezone(timezone.utc).strftime("%Y-%m-%d")))
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('$R_{rs} \ (m^{-1})$')
    ax.grid()
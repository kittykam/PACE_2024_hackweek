import earthaccess
import xarray as xr
from xarray.backends.api import open_datatree
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from datetime import datetime, timezone
from random import randint
auth = earthaccess.login(persist=True)


def Rrs_avg(flag, lat_N, lat_S, lon_W, lon_E):
    tspan = ("2024-07-19", "2024-08-03")
    results = earthaccess.search_data(
        short_name="PACE_OCI_L3M_RRS_NRT",
        temporal=tspan,
        granule_name="*.8D.*.0p1deg.*",
    )

    paths = earthaccess.open(results)

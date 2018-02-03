class PathSection:

    def __init__(self, ats_ident, seq_nbr, dir, type, icao, bidirect, freq_class, level, status,
                 wpt1_icao, wpt1_nav_type, wpt1_ident, wpt1_ctry, wpt1_desc_1, wpt1_desc_2,
                 wpt1_desc_3, wpt1_desc_4, wpt1_wgs_lat, wpt1_wgs_dlat, wpt1_wgs_long, wpt1_wgs_dlong,
                 wpt2_icao, wpt2_nav_type, wpt2_ident, wpt2_ctry, wpt2_desc_1, wpt2_desc_2, wpt2_desc_3,
                 wpt2_desc_4, wpt2_wgs_lat, wpt2_wgs_dlat, wpt2_wgs_long, wpt2_wgs_dlong, outbd_crs,
                 distance, inbd_crs, min_alt, upper_limit, lower_limit, maa, cruise_level, rnp,
                 cycle_date, rvsm, fix_turn1, fix_turn2):
        self.ats_ident = ats_ident
        self.seq_nbr = seq_nbr
        self.dir = dir
        self.type = type
        self.icao = icao
        self.bidirect = bidirect
        self.freq_class = freq_class
        self.level = level
        self.status = status
        self.wpt1_icao = wpt1_icao
        self.wpt1_nav_type = wpt1_nav_type
        self.wpt1_ident = wpt1_ident
        self.wpt1_ctry = wpt1_ctry
        self.wpt1_desc_1 = wpt1_desc_1
        self.wpt1_desc_2 = wpt1_desc_2
        self.wpt1_desc_3 = wpt1_desc_3
        self.wpt1_desc_4 = wpt1_desc_4
        self.wpt1_wgs_lat = wpt1_wgs_lat
        self.wpt1_wgs_dlat = wpt1_wgs_dlat
        self.wpt1_wgs_long = wpt1_wgs_long
        self.wpt1_wgs_dlong = wpt1_wgs_dlong
        self.wpt2_icao = wpt2_icao
        self.wpt2_nav_type = wpt2_nav_type
        self.wpt2_ident = wpt2_ident
        self.wpt2_ctry = wpt2_ctry
        self.wpt2_desc_1 = wpt2_desc_1
        self.wpt2_desc_2 = wpt2_desc_2
        self.wpt2_desc_3 = wpt2_desc_3
        self.wpt2_desc_4 = wpt2_desc_4
        self.wpt2_wgs_lat = wpt2_wgs_lat
        self.wpt2_wgs_dlat = wpt2_wgs_dlat
        self.wpt2_wgs_long = wpt2_wgs_long
        self.wpt2_wgs_dlong = wpt2_wgs_dlong
        self.outbd_crs = outbd_crs
        self.distance = distance
        self.inbd_crs = inbd_crs
        self.min_alt = min_alt
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.maa = maa
        self.cruise_level = cruise_level
        self.rnp = rnp
        self.cycle_date = cycle_date
        self.rvsm = rvsm
        self.fix_turn1 = fix_turn1
        self.fix_turn2 = fix_turn2
import timesynth as ts

time_sampler = ts.TimeSampler()
irregular_time_samples = time_sampler.sample_irregular_time(num_points=500, keep_percentage=50)

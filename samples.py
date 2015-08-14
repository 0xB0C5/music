def wave_to_samples(wave, time, sample_rate):
	n_samples = int(time * sample_rate)
	return [wave(float(i)/sample_rate) for i in range(n_samples)]
	
def samples_to_wave(samples, sample_rate):
	def wave(x):
		index = int(x*sample_rate)
		if 0 <= index < len(samples):
			return samples[index]
		else:
			return 0
			

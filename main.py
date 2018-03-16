import speech_recognition as sr

mic_name = "Bus 001 Device 002: ID 0cf3:e301 Qualcomm Atheros Communications "
samprate = 48000
cs = 2048

r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
for i, microphone_name in enumerate(mic_list):
	if microphone_name == mic_name:
		device_id = 1

with sr.Microphone(device_index = device_id, sample_rate = samprate, chunck_size=cs) as  source:
	r.adjust_for_ambient_noise(source)
	print('Speak Biatch')
	audio = r.listen(source)
	
	try:
		t = r.recognice_google(audio)
		print(t)
	except:
		print('Error')

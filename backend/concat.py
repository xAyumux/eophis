import os
import wave

def join_waves(inputs):
    '''
    inputs : list of filenames
    '''
    temp_wav_folder = "./tmp"
    os.makedirs(temp_wav_folder, exist_ok=True)
    output = temp_wav_folder + "/"+'concat.wav'
    
    try:
        fps = inputs
        fpw = wave.open(output, 'w')

        fpw.setnchannels(fps[0].getnchannels())
        fpw.setsampwidth(fps[0].getsampwidth())
        fpw.setframerate(fps[0].getframerate())
        
        for fp in fps:
            fpw.writeframes(fp.readframes(fp.getnframes()))
            fp.close()
        fpw.close()

    except wave.Error:
        print("wave.Error") 

    except Exception:
        print("other error")

if __name__ == '__main__':
    inputs = ["onsei.wav","test.wav"]
    output = 'output.wav'
    inputs = [wave.open(f, 'r') for f in inputs]
    import pdb;pdb.set_trace()
    join_waves(inputs)
    print("finish")

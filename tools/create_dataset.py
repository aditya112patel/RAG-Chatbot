import pandas as pd

non_informational_words = [
    'hello', 'hi', 'hey', 'greetings', 'goodbye', 'bye', 'thank you', 'thanks', 'please',
    'morning', 'evening', 'night', 'how are you', 'what’s up', 'see you', 'take care',
    'no problem', 'okay', 'cool', 'sure', 'alright', 'good', 'nice', 'awesome', 'great',
    'fine', 'yes', 'no', 'maybe', 'alrighty', 'okay then', 'see ya', 'goodnight', 'good morning',
    'hi there', 'what’s going on', 'good to see you', 'good day', 'peace', 'later', 'hello again',
    'talk to you later', 'see you soon', 'catch you later', 'good afternoon', 'take it easy',
    'how’s it going', 'how’s everything', 'what’s new', 'how do you do', 'how’s life',
    'hope you’re well', 'thanks a lot', 'thanks so much', 'thanks for that', 'much appreciated',
    'thank you so much', 'thank you very much', 'thanks a million', 'thanks anyway',
    'no worries', 'don’t mention it', 'that’s alright', 'all good', 'I’m fine', 'I’m good', 'not bad',
    'I’m okay', 'doing well', 'I’m great', 'I’m awesome', 'feeling good', 'so long', 'see you later',
    'take care of yourself', 'see you around', 'catch you soon', 'have a good one', 'bye for now',
    'have a nice day', 'have a great day', 'see you in a bit', 'stay safe', 'be well', 'be careful',
    'enjoy your day', 'take care now', 'good to meet you', 'it’s been nice', 'good talking to you',
    'it’s a pleasure', 'it’s been a pleasure', 'pleasure meeting you', 'hope to see you soon',
    'we’ll catch up later', 'talk later', 'keep in touch', 'I’m out', 'it’s all good', 'I’m off',
    'see you soon', 'let’s catch up', 'cheers', 'you too', 'have a good night', 'sweet dreams',
    'until next time', 'see you next time', 'let’s talk soon', 'talk soon', 'take it easy', 'so far so good',
    'everything’s good', 'all is well', 'I’m doing fine', 'glad to hear', 'I’m happy for you', 'that’s nice',
    'sounds good', 'sounds great', 'sounds awesome', 'feels good', 'that’s cool', 'that’s awesome',
    'that’s great', 'nice to hear', 'good stuff', 'looking good', 'feeling better', 'feeling fine', 
    'feeling great', 'I’m okay', 'that’s okay', 'it’s okay', 'no problem at all', 'sure thing',
    'you’re welcome', 'my pleasure', 'happy to help', 'glad I could help', 'don’t worry', 
    'you bet', 'anytime', 'absolutely', 'no big deal', 'no issues', 'not a problem', 
    'yup', 'yeah', 'nah', 'nope', 'sure', 'yep', 'definitely', 'indeed', 'certainly', 
    'alright then', 'good call', 'good move', 'well done', 'great job', 'nice work', 
    'that’s fantastic', 'that’s wonderful', 'perfect', 'that’s perfect', 'excellent', 
    'brilliant', 'fantastic', 'amazing', 'lovely', 'spot on', 'you got it', 'you nailed it', 
    'bingo', 'bullseye', 'exactly', 'precisely', 'right on', 'no problem at all', 
    'you’re spot on', 'you’re right', 'that’s right', 'couldn’t agree more'
]

informational_words=['sound', 'wave', 'medium', 'fig', 'waves', 'called', 'e', 'pr', 'speed', 'frequency', 'one', 'time', 
 'hearing', 'hear', 'vibrating', 'distance', 'ultrasound', 'particles', 'used', 'shown', 'density', 
 'c', 'r', 'w', 'ear', 'object', 'hz', 'reflection', 'source', 'air', 'travel', 'unit', 'produced', 
 'high', 'compressions', 'v', 'reflected', 'ultrasonic', 'also', 'thr', 'rarefactions', 'different', 
 'given', 'value', 'wavelength', 'pitch', 'may', 'range', 'energy', 'fr', 'back', 'travels', 
 'objects', 'pressure', 'two', 'frequencies', 'loudness', 'aid', 'tuning', 'fork', 'ound', 'thus', 
 'amplitude', 'q', 'l', 'get', 'electrical', 'metal', 'sounds', 'water', 'n', 'essur', 'due', 
 'propagation', 'direction', 'higher', 'reflecting', 'audible', 'ultrasounds', 'like', 'light', 
 'change', 'produce', 'take', 'cience', 'disturbance', 'moves', 'move', 'human', 'point', 'slinky', 
 'know', 'surface', 'maximum', 'taken', 'khz', 'echo', 'infrasound', 'signals', 'detect', 'etc', 
 'ou', 'near', 'table', 'ball', 'small', 'big', 'ough', 'observe', 'position', 'low', 'make', 
 'per', 'propagates', 'number', 'able', 'longitudinal', 'transverse', 'b', 'even', 'represented', 
 'period', 'solution', 'ms', 'person', 'intensity', 'hall', 'generally', 'amplified', 'parts', 
 'ar', 'mechanical', 'om', 'activity', 'end', 'happens', 'particle', 'oduced', 'variations', 
 'uestion', 'friend', 'regions', 'example', 'well', 'consecutive', 'complete', 'temperature', 
 'pipes', 'heard', 'reverberation', 'body', 'heart', 'block', 'various', 'ener', 'gy', 'ears', 
 'another', 'form', 'transmitted', 'rubber', 'friends', 'ead', 'gets', 'motion', 'oduce', 
 'hence', 'region', 'egion', 'compr', 'instrument', 'solid', 'average', 'hertz', 'later', 'si', 
 'equency', 'depends', 'minimum', 'oscillation', 'second', 'associated', 'louder', 'uestions', 
 'successive', 'quality', 'media', 'angles', 'clock', 'thunder', 'properties', 'must', 'cliff', 
 'medical', 'curved', 'halls', 'animals', 'bat', 'electronic', 'microphone']


labels = [1] * len(informational_words) + [0] * len(non_informational_words) 

data=pd.DataFrame()
data['text']=informational_words+non_informational_words
data['label']=labels

data.to_csv('dataset.csv',index=False)
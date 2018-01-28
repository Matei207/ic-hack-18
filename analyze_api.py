########### Python 3.6 #############
import requests, base64

def run_api():
    headers = {
        # Request headers.
        'Content-Type': 'application/octet-stream',

        # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
        'Ocp-Apim-Subscription-Key': '224997f32ee14a6781a3107cfea5ce67',
    }

    params = {
        # Request parameters. All of them are optional.
        'visualFeatures': 'Categories, Description, Tags',
        'language': 'en',
    }

    # Replace the three dots below with the full file path to a JPEG image of a celebrity on your computer or network.
    image = open('/Users/mateidavid/Workspace/Hackathons/ic-hack-18/20180128_043409.jpg','rb').read() # Read image file in binary mode

    try:
        # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the
        #   URL below with "westus".
        response = requests.post(url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze',
                                 headers = headers,
                                 params = params,
                                 data = image)
        data = response.json()
        return data
        #print(data)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    ####################################

def select_highest_confidence(data):
    highest_confidence = 0.1
    confidence_index = None
    for i in range(0,len(data['description']['captions'])):
        #list with captions from microsoft api
        confidence = data['description']['captions'][i]['confidence']
        if highest_confidence < confidence:
            highest_confidence = confidence
            confidence_index = i
        return confidence_index

def output_description(data, index):
    entry = data['description']['captions'][index]
    confidence = entry['confidence']

    if confidence >= 0.7:
        return 'Pretty sure that it is a ' + entry['text']
    elif confidence > 0.3 and confidence <= 0.6:
        return 'Could be a ' + entry['text']
    else:
        return 'Not sure. Might be ' + entry['text']

def image_init():
    data = run_api()
    high_index = select_highest_confidence(data)
    return output_description(data, high_index)

print(image_init())




def call_emotion_api(source):

    import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json

    #define dictionary
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        #data: must contain binary vector of picture
        'Content-Type': 'application/octet-stream',
        #'Content-Type': 'application/json', #alternative for URL's
        #AZURE KEY:
        'Ocp-Apim-Subscription-Key': 'XXXXXXXXX', #insert subscription key
    }
    
    #params: if face rectangles are provided by user
    params = urllib.parse.urlencode({
    })
    
   
    try:    
        body = open(source, "rb").read()
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read() 
        #print(data)
        conn.close()
        #return json.loads(data.decode('utf8'))
        return data.decode('utf8')
    except Exception as e:
        print(e.args)
        return(e.args)

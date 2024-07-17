# FlightFinder

- Flightfinder can be used to keep a track on the ticket prices of your desired flights
- To do this, it utilizes Teqila API for obtaining flight details, Twilio API for SMS and SHEETY API for interacting with google sheets
- Enter your source destination and desired flight in the ticket, there can be multiple such rows
- On running, the script goes throught these rows iteratively and comapares the actual market price to the threshold price. You'll get a message on your phone and email (using smtp)
- The running can be automated by uploading this on [PythonAnywhere](https://pythonanyhwhere.com)

- Steps to Install
    - Open your terminal in the project directory
    
    ``` git clone https://github.com/sahil-s-246/Flight-Finder.git ```

    - Create a ```val.cfg``` file
    - Sections are created in it according to the first letters of the file name
     ```
    [datman]
    Sheety_endpoint = <API_KEY>
    ```
    -Likewise enter your API keys, Twilio Credentials and email and phone details for smtp and twilio respectively
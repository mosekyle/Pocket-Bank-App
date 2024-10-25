# Welcome to Cloud Functions for Firebase with Python!
# To get started, you can use this template as a foundation.
# Deploy the function using: `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app, credentials
from firebase_functions.https_fn import Request, Response

# Initialize Firebase Admin SDK with error handling
try:
    # If you have specific credentials, provide the path to your service account JSON file
    # Uncomment and replace `path/to/serviceAccount.json` if needed
    # cred = credentials.Certificate('path/to/serviceAccount.json')
    # initialize_app(cred)
    
    # Initialize with default application credentials
    initialize_app()
    print("Firebase Admin SDK initialized successfully.")
except Exception as e:
    print(f"Failed to initialize Firebase Admin SDK: {e}")

# Sample HTTP Function to handle web requests
@https_fn.on_request()
def on_request_example(req: Request) -> Response:
    """
    Sample HTTP function that responds to a web request.
    
    Args:
        req (https_fn.Request): The incoming HTTP request.
    
    Returns:
        https_fn.Response: The HTTP response.
    """
    try:
        # Simple response for demonstration purposes
        message = "Hello, World! You've deployed your first Firebase Function with Python!"
        return Response(message, status=200)
    except Exception as e:
        # Handle any unexpected errors and respond accordingly
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return Response(error_message, status=500)

import gspread
from google.oauth2.service_account import Credentials


# Constants copied from google API documentation
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# Other required constant settings created by you developer
# Note use of capslock to indicate those values don't change
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


# Function to collect sales data from client/user
def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    # Note by default, data input is entered as string at terminal
    # Hence need to split them using comma (,)
    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")
    validate_data(sales_data)


# Function to validate collected sales data from client/user
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    # Try 2 conditions - value as integer, then max of 6 figures
    # Raise ValueError if any condition fails
    try:
        # This first line converts input values to integer
        [int(value) for value in values]

        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


# Call out get_sales_data function.
# Note validate function is already inserted in it above
get_sales_data()

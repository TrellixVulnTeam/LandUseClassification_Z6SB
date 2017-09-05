# Server constants
DB_DRIVER = "ODBC Driver 13 for SQL Server"
SERVER_NAME = "TYLER-LAPTOP\TYLERSQLSERVER"
PORT_NUMBER = "21816"
DATABASE_NAME = "land_use_database"

# Path to images
IMAGE_DIR = "\\\\Tyler-laptop\\tylersqlserver\\FileTableData\\"	# TODO: change to FILETABLE_DIR
REPO_DIR = "C:\\Users\\t-tyrome\\Documents\\Internship\\LandUseClassification"

# Class label mapping
LABELS = {
	"Barren": 0,
	"Forest": 1,
	"Shrub": 2,
	"Cultivated": 3,
	"Herbaceous": 4,
	"Developed": 5
}

#Tables
TABLE_TRAIN_FEATURES = "dbo.train_features"
TABLE_VALIDATION_FEATURES = "dbo.validation_features"
TABLE_TEST_FEATURES = "dbo.test_features"
TABLE_VAL_PREDICTIONS = "dbo.val_predictions"
TABLE_TEST_PREDICTIONS = "dbo.test_predictions"
TABLE_MODELS = "dbo.models"

# Variables
MICROSOFTML_MODEL_NAME = "Resnet18"
FASTTREE_MODEL_NAME = "rx_fast_trees"
LAND_USE_CSV = "land_use.csv"

#Functions
def get_connection_string():
	driver = "DRIVER={" + DB_DRIVER + "}"
	port = "PORT=" + PORT_NUMBER
	server = "SERVER=" + SERVER_NAME
	database = "DATABASE=" + DATABASE_NAME
	trusted = "Trusted_Connection=Yes"
	connection_string = ";".join([driver,server,port,database,trusted])
	print(connection_string)
	return connection_string


import json
import os

from openpyxl import Workbook
from openpyxl import load_workbook

# PyApacheAtlas packages
# Connect to Atlas via a Service Principal
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient  # Communicate with your Atlas server
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader




if __name__ == "__main__":
    """
    This sample provides an end to end sample of reading an excel file,
    generating a batch of entities, and then uploading the entities to
    your data catalog.
    """

    # Authenticate against your Atlas server
    oauth = ServicePrincipalAuthentication(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID", ""),
        client_secret=os.environ.get("CLIENT_SECRET", "")
    )
    client = PurviewClient(
        account_name = os.environ.get("PURVIEW_NAME", ""),
        authentication=oauth
    )

    # SETUP: This is just setting up the excel file for you
    file_path = "./demo_bulk_entities_upload_2.xlsx"
    excel_config = ExcelConfiguration()
    excel_reader = ExcelReader(excel_config)

    # Create an empty excel template to be populated
    excel_reader.make_template(file_path)
    # This is just a helper to fill in some demo data


    # ACTUAL WORK: This parses our excel file and creates a batch to upload
    entities = excel_reader.parse_bulk_entities(file_path)

    # This is what is getting sent to your Atlas server
     print(json.dumps(entities,indent=2))

    results = client.upload_entities(entities)

   # print(json.dumps(results, indent=2))

    print("Completed bulk upload successfully!\nSearch for hivetable01 to see your results.")

import itertools
import json
import os
from xml.etree.ElementTree import tostring

from openpyxl import Workbook
from openpyxl import load_workbook

# PyApacheAtlas packages
# Connect to Atlas via a Service Principal
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient  # Communicate with your Atlas server
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader


if __name__ == "__main__":
    ""
 

    # Authenticate against your Atlas server
    oauth = ServicePrincipalAuthentication(
        tenant_id=os.environ.get("TENANT_ID", "TENANT_ID"),
        client_id=os.environ.get("CLIENT_ID", "CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET", "CLIENT_SECRET")
    )
    client = PurviewClient(
        account_name = os.environ.get("PURVIEW_NAME", "PURVIEW_NAME"),
        authentication=oauth
    )


    #Here I am getting the entire definition of the object.
    response = client.get_single_entity("84495095-8923-4477-a179-bd2f2dccbad8")
    
    print(json.dumps(response, indent=2))

    #here I set the attribute details
    business_data = {"TestAttributeGroup":{
                            "TestAttribute":"Mytestvalue2"
                        }}
    
    print(business_data)
    #here I call the update_businessmetadata function passing the guid of the asset. 
    response = client.update_businessMetadata("84495095-8923-4477-a179-bd2f2dccbad8",business_data)


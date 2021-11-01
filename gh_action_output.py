import json
from ansible_navigator._yaml import human_dump

class Gh_Action_Output():

    def __init__(self, serialization="yaml"):
        self._serialization = serialization

    def error(self, message):
            print(f"::error::{message}")

    def group(self, title:str, content:str = "", decorate: str = "", asterisk: bool=True, ):
        if asterisk:
            asterisk = " " + ("*" * (66- len(title)))
        else:
            asterisk = ""
        
        decor = ""
        if decorate == "check":
            decor = "\u2705"
        elif decorate == "cross":
            decor = "u274c"
        else:
            raise ValueError(f"decoration '{decorate}' %s not supported")
        
        if decor:
            decor += " "

        print(f"::group::{decor}{title}{asterisk}")
        for line in self._serialize(content).splitlines():
            print(f"{line}")
        print("::endgroup::")
    
    def notice(self, message):
        print(f"::notice::{message}")
    
    def warning(self, message):
        print(f"::warning::{message}")
    
    def _serialize(self, content):
        if isinstance(content, (list, dict)):
            if self._serialization == "yaml":
                return human_dump(content)
            elif self._serialization == "json":
                return json.dumps(content, indent=4, sort_keys=True)

        return content

   



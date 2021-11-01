import json
from ansible_navigator._yaml import human_dump

class Gh_Action_Output():

    def __init__(self, serialization="yaml"):
        self._serialization = serialization

    def error(self, message):
            print(f"::error::{message}")

    def group(self, title:str , content:str = ""):
        print(f"::group::'\033[31;1;4m{title}\033[0m'")
        print(self._serialize(content))
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

   



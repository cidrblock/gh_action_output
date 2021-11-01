
from gh_action_output import Gh_Action_Output

def main():
    with open ("task_output.yaml", "r") as fhand:
        data=fhand.read()
        
    gh = Gh_Action_Output(serialization="json")

    gh.group("TASK [Gathering Facts:localhost_1]", data)
    gh.group("TASK [Gathering Facts:localhost_2]", data)
    gh.group("TASK [Gathering Facts:localhost_3]", data)
    gh.group("TASK [Gathering Facts:localhost_4]", data)
    gh.group("TASK [Do this:localhost_1]", data)
    gh.group("TASK [Do this:localhost_2]", data)
    gh.group("TASK [Do this:localhost_3]", data)
    gh.group("TASK [Do this:localhost_4]", data)
    gh.error("TASK [Do this:localhost_4]")

    play = """
    localhost_1                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    localhost_2                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    localhost_3                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    localhost_4                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
    """

    gh.group("PLAY RECAP", play)

    # gh.notice("notice message")

    # gh.warning("warning message")

    # gh.group("group 2", {1:2})

if __name__ == "__main__":
    main()
 
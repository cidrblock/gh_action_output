
from gh_action_output import Gh_Action_Output

def main():
    with open ("gather_output.yaml", "r") as fhand:
        gather=fhand.read()
    
    with open ("set_fact_output.yaml", "r") as fhand:
        fact=fhand.read()
        
    gh = Gh_Action_Output(serialization="json")

    gh.group("TASK [Gathering Facts:localhost_1]", content=gather, decorate="check")
    gh.group("TASK [Gathering Facts:localhost_2]", content=gather, decorate="check")
    gh.group("TASK [Gathering Facts:localhost_3]", content=gather, decorate="check")
    gh.group("TASK [Gathering Facts:localhost_4]", content=gather, decorate="check")
    gh.group("TASK [Do this:localhost_1]", content=fact, decorate="check")
    gh.group("TASK [Do this:localhost_2]", content=fact, decorate="check")
    gh.group("TASK [Do this:localhost_3]", content=fact, decorate="check")
    gh.group("TASK [Do this:localhost_4]", content=fact, decorate="cross")

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
 
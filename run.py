
from gh_action_output import Gh_Action_Output

def main():
        
    gh = Gh_Action_Output(serialization="json")

    gh.group("group 1", {1:2})

    gh.error("error message")

    gh.notice("notice message")

    gh.warning("warning message")

    gh.group("group 2", {1:2})

if __name__ == "__main__":
    main()
    print("::group::Wrapper")

    print("Wrapper begin")

    print("::group::Foo")
    print("Foo")
    print("::endgroup")

    print("Something")

    print("::group::Bar")
    print("Bar")
    print("::endgroup")

    print("Wrapper end")

    print("::endgroup::")
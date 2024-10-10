from src.sample_classes_project.core import Project, Project2


if __name__ == "__main__":

    # get info about which project scenario run
    # if scenario1:
    moj_projekt = Project(param1=10, param2=20)
    result = moj_projekt.process(data=12)
    print(f"Result: {result}")

    #elif scenario2:
    moj_projekt2 = Project2(param1=10, param2=20,param3=30)
    result = moj_projekt2.process(data=12)
    print(f"Result: {result}")


    # Jakbysmy to napisali funkcjonalnie to musielibyśmy na kazdej roznicy pomiedzy projektami robić if'y
    # input_data = 12
    # result = calculate_something()
    # if scenario1:
    #     result = calculate_something_project
    # elif scenario2:
    #     result = calculate_something_project2

    # itd...
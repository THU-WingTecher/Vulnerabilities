import datetime
from pytz import timezone
LOCATION = 'Asia/Shanghai' # 'Asia/Seoul'
SHORT_LOCATION = 'CST'

def get_url(file_name: str) -> str :
    return f"https://github.com/THU-WingTecher/Vulnerabilities/res/{file_name}"

def get_rel_path(file_name: str) -> str :
    return f"res/{file_name}"

class Writer() :
    def __init__(self) -> None:
        self.path = "Readme.md"
        pass
    
    def dump(self) -> None :
        contents = self.write() 
        with open(self.path, "w") as file :
            file.write(contents)
    
    def load(self) -> str :
        with open(self.path, "r") as file :
            return file.read()

    def get_date() :
        # Get the current date
        current_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if current_date.hour+9 >= 24:
            timezone_time = current_date.hour+9-24
        else :
            timezone_time = current_date.hour+9

        currdate = current_date.replace(hour=timezone_time)
        currdate = currdate.replace(second=0)
        currdate=currdate.replace(tzinfo=timezone(LOCATION))
        return f'Last updated : {currdate.strftime("%A, %d %b, %H:%M")} {SHORT_LOCATION}'
    
    def introduce(self) -> str :
        return f"We detect 1000+ bugs for OS(linux, ROS, etc), database(MariaDB, MySQL, etc), block-chain, protocol systems as well as OSS projects."
    
    def addintional_info(self) -> str :
        return ""
        # return f"[Additional information or conclusion about the projects tested and the impact of your bug-finding capabilities.]"
    def write(self) -> str :
        #FIXME How to validate the file name is right?
        return f"""
## Introduction
{self.introduce()}

![Total Bugs Found]({get_rel_path('overall.png')})
For detailed information on the bugs we've identified, visit the following links:
- [CVE Details]({get_rel_path('CVE.md')})
- [CNVD Details]({get_rel_path('CNVD.md')})
- [Other Bugs Details]({get_rel_path('others.md')})

"""
# ![Total Projects Tested]({get_rel_path('num_of_tested_projects.png')})
# {self.addintional_info()}
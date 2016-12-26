import xml.dom.minidom

def main():
    # load and parse an XML file
    doc = xml.dom.minidom.parse(r"F:\Github\Python\Practice\Files\data\sample.xml")

    # print the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # get a list of XML tags
    skills = doc.getElementsByTagName("skill")
    print("%d skills:" % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    # create a new tag
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "Ruby")
    doc.firstChild.appendChild(newSkill)

    print("")
    skills = doc.getElementsByTagName("skill")
    print("%d skills:" % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

if __name__ == "__main__":
    main()
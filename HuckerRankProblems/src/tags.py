
# Task: we have a array of strings with information. We have to find all unique
# tags and print them in descending order by count. Tags are the last part of the
# string ("tag1:09,tag2:1,tag3:123") and delimited by ','
# We have an assumption all strings are correct. There is no need to check for errors.

# Example:
# someString:someText|text:9|tag1:09,tag2:1,tag3:123
# someString1:someText|text:9|tag1:09,tag4:1,tag5:123
# someString1:someText|text:9|tag1:09,tag2:1,tag6:123

# Output:
# 3 tag1:09
# 2 tag2:1
# 1 tag6:123
# 1 tag3:123
# 1 tag5:123
# 1 tag4:1


class TagElement:
    tag = None
    count = None

    def __init__(self, tag, count):
        self.tag = tag
        self.count = count

def sortedTags(strings):
    if strings is None:
        return

    delim1 = "|"
    delim2 = ","
    tagsIndex = 2

    # will store our unique results
    resDict = dict()

    # check all strings in array
    for str in strings:
        tags = str.split(delim1)[tagsIndex]

        # now get the tags.
        tags = tags.split(delim2)
        for tag in tags:
            tag = tag.lower()

            if tag in resDict:
                resDict[tag] += 1
            else:
                resDict[tag] = 1
        # end of for tags
    # end of for strings

    # add results to the list
    sortedList = list()
    for key in resDict:
        sortedList.append(TagElement(key, resDict[key]))

    # sort the list.
    sortedList = sorted(sortedList, key=lambda tagObj: tagObj.count, reverse=True)

    # print the result
    for elem in sortedList:
        print("{0} {1}".format(elem.count, elem.tag))


if __name__ == "__main__":
    strings = list()
    strings.append("someString:someText|text:9|tag1:09,tag2:1,tag3:123")
    strings.append("someString1:someText|text:9|tag1:09,tag4:1,tag5:123")
    strings.append("someString1:someText|text:9|tag1:09,tag2:1,tag6:123")
    sortedTags(strings)
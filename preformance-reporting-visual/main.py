#!/usr/bin/env python

import matplotlib.pyplot as plt
import json
import os

#TODO: Create global array of domains: Create global array of  [site-speed:SEO:Best Practices]
domains = []
score = []
extra = []

def main():
    global domains
    global score
    global extra
    print("Main() init")
    for index, filename in enumerate(os.listdir((os.getcwd()+"/reports/"))):
        f = open(os.getcwd() + "/reports/" + (filename), "r")
        contents = f.read()
        fContents = json.loads(contents)
        domains.append(filename.split('.')[0])
        score.append(int(fContents['reportCategories'][3]['score']))
        extra.append(index)
    barplot(extra, score, 0, "Domains", "Google best practices score per domain")

def barplot(x_data, y_data, error_data, x_label="",title=""):
    _, ax = plt.subplots()
    # Draw bars, positions them in center of the tick mark on the x-axis
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')

    ax.set_ylabel("Score")
    ax.set_xlabel(x_label)
    ax.set_title(title)
    plt.xticks(extra, domains)
    plt.xticks(rotation=90)
    plt.show()

if __name__ == '__main__':
    main()

# COMP370 final exam summary

---
---
---

## important concepts
- **data science project phases**:
    - *question definition* (what to measure)
        - iterative process. statement of something we want to measure. refined!
        - find a representative stakeholder -> develop a use case -> iterate on the question
    - *data collection* (how to measure)
        - obtaining and arranging data (collect, clean, correct, standardize)
        - collect the data (download, scrape, api) -> clean the data (remove duplicates, missing values, outliers, format) -> organize the data (format, structure, store)
        - *found data* vs *designed data*
    - *data annotation* (infer/add feature to make measure clearer)
        - applying/inferring features
        - tasks: devising the labels to use and assigning the labels to the data
        - properties: real-valued or categorical (classifications)
        - *typology*: comprehensive, sharply-defined, objective-ish categorization system
            - *building typology*: get representative data -> get typology or build one -> sanity check yourself -> human test with expert coders -> does it work? if not go back to 2, else move on
        - *open coding*: take sample of data, code it and look for patterns -> create categories (iterate)
        - *human coding*: process of assigning labels 
            - *expert coding* vs *crowdsourcing* 
            - ethics: capacity of harm!
            - *training*: prepare a code book (typology definition document) -> provide challenging examples -> run the group sessions
            - *human coding process*: preparation phase (decide groups, develop code book, training material, annotations software) -> annotation phase (recruit coders, run training sessions, coders code data) -> validation phase (assess quality and level of agreement)
            - *annotation quality - level of agreement*: perfect/majority/no majority agreement
            - *annotator agreement*: confusing typology/bad coder/tricky cases/human error
        - *automated annotation*: using algorithm 
        -*precise answers*: statement that provides all the details audience requires in order to use the info in a wide array of contexts. factors: question objective (what=definition, how=explanation/process, why=motivation), level of detail expected by the audience
    - *data analysis* (measuring)
        - stats models/visualizations using existing methods and existing clean quantitative data
        - data science builds new things/innovation
        - *fishing expedition*: when you don't have a question, just looking at data to see what you can find. ask questions that  narrow the open ended question to bound it -> analysis should have a concetre outcome/insight in mind, else if no target insight you are fishing -> result attempt to support insight
        - *result*: a claim that can be directly verified using a process and data. to be valid, need valid data + valid method
    - *interpretation* (how to understand)
        - evidence != answer. interpretation is about using evidence to support a conclusion 
        - *structure*: restate the original question + key big points takeaways with eveidence to validate it + concluding section that draws on main points 
        - *key points technique*: assert contextualization -> include negative outcomes -> support by combing results + extrapolating from results -> use points to make a meta point (conclusion)
        - *interpretation approach*: write out big ppints that stand out -> decide on a rough conclusion that fits -> write out arguments for each point -> if arguments need more evidence loop back to analysis, else if evidence supports another point loop back -> refine the conclusion
    - *communication* (share)
        - communication == persuasion == story
        - remember the audience
        - *visualization*: to support the storytelling. necessary details: readable + title + caption
        - *written reports*:
            - motivation
            - objective/problem
            - data
            - design/methods
            - resuts
            - findings/interpretation/discussion
            - conclusion
        - *presentation*: relatable opening + technical written report stucture. be relatable, tell a story, highlight main point, make it engaging
- **unix**:
    - programs that do one thing well
    - programs that work well together
    - programs that can handle text streams
- **working with data**: exploration + scale + visualization
- **cloud**:
    - disadvantages of not cloud: limited compute power, limited special hardware, limited storage, insecure, poor proximity to resources, uptime
    - virtual machines: close to power plants, can grab data quickly
- **EC2/ssh keys**:
    - AWS account -> ssh key pair (`ssh-keygen`) -> create lightsail instance -> `ssh -i .ssh/<instance_name> unbuntu@<IP address>`
- **user creation**:
    - `ssh <IP address>` -> `sudo adduser <username>` -> `sudo usermod -aG <username>` -> `su <username>` -> `mkdir .ssh` -> `chmod 700 .ssh` -> `cd .ssh` -> copy the id_rsa.pub key -> `vim authorized_keys` and paste it -> `ssh <IP address>`
- **tmux**: working remote `tmux new -s <name>` and `tmuz attach -t <name>`
- **webserver**: `ssh <IP address>` -> `sudo apt install apache2` -> `sudo systemctl enable apache2` -> `sudo vim /etc/apache2/ports.conf` Listen 8008 -> `sudo vim /etc/apache2/sites-available/000-default.conf` virtual host*:8008 -> `sudo vim /var/www/html/comp370_hw2.txt` Hello world ->`sudo systemctl restart apache2` -> instance, firewall ipv4, add rule, custom, TCP, 8008 -> access using localhost:8008/comp370_hw2.txt
- **database**: `ssh <IP address>` -> `sudo apt install mariadb-server -y` -> `sudo systemctl enable mariadb` -> `sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf` port 6002 change bind address = 0.0.0.0 -> `sudo systemctl restart mariadb` -> `sudo mysql` -> CREATE DATABSE; CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s'; GRANT PRIVILEGES ON comp370 * TO 'comp370'@'%'; FLUSH PRIVILEGES; -> instance, ipv4 firewall, add rule, custom TCP 6002 -> `sudo systemctl restart mariadb`
- **core tools**:
    - exploration + expressivness + reproduceability + collaboration + communication
- **project structure**: project name - README (welcome, overview, goals, TODOs, GOTCHAs, installation, run instructions) + data dir + src dir (implemented function code) + scripts dir (interaction with code)
- **python**: scripts = program, built-in types, libraries 
- **reasons/ways for coding**:
    - exploration (trying things out)
    - tool building (scripts, automation, packaging)
    - pipelining (automations, big projects)
- **jupyter notebook**: intall jupyter on EC2 -> launch vscode -> in terminal, launch jupyter and note down port number -> in port forwarding list, add port number -> open browser and paste URL+token
- **bokeh**: data prep (get the data and filter it) -> import bokeh -> read and sort the data -> create select widgets -> create the figures (title, x/y-axis) with labels -> init the data source -> plot first set of data (.line ...) -> setup legend and layout -> update function (callback) -> attach callback to select widgets -> define layout, curdoc().add_root(layout) -> bokeh serve --port 8888 --show file_name.py
- **modularization**: grouping by functionality (functions, classes, modules, packages)
- **redundant code**: hard to maintain + hard to read + code bloats. recognize it + group into functions generalized + break longer functions into smaller ones + use collections 
- **dabbling**: identify critical parts -> write just enough code to check if its the right approach -> try to accomplish critical part with different tool -> iterate (dont get committed)
- **refactoring**: reorganizing the structure of the code without changing the functionality (renaming variables, breaking down long functions, grouping similar functions, removing redundant code, changing libraries, altering function contracts...)
- **api data collection**: construct URL+params -> call the URL -> receive the data -> store the data -> loop back if needed
- **scraping**: *static site scraping* (wget, curl, requests, bs4) vs *dynamic site scraping* (bs4, selenium)
    - scraping with cache: check if cache exists -> if yes use it else scrape the page and save the cache and then use the cache -> soup = bs4.BeautifulSoup(hmtl, 'html.parser') -> find the elements (soup.find_all(), soup.find()) using the html tags -> extract the data and format it -> save the data (json.dump())
- **sampling**: taking a subset of the data, more manageable, easier to understand and faster to process
    - *systematic sampling by id* vs *snowball sampling*
- **bias**: disproportinately weight factors that impact measurements
- **tf-idf**: term frequency inverse document frequency (tf-idf(term, document, Documents) = tf(term, document) * idf(term, Documents), where idf(term, Documents) = log(total_num_catgories / (|{document in Docments: term in document}|)))
- **networks**:
    - nodes, edges, weights, paths
    - centrality (how important in the network), degree (connected), closeness (number of hops to others), betweeness (essentialness, fraction of all shortest paths in the network that pass through the node)
    - communities/clustering: how to group nodes. *modularity*: the ratio of the number of edges inside vs outside the cluster
- **career**: nobody knows all the tools, keep learning, adapt, social network (develop and maintain a professional network), don't get discouraged

---

## important coding examples
```
- argparse
- CLI + csvtool
- unittests
- bokeh
- python requests for api calls
- json
- tf-idf
- network analysis (hw12)
```

---
---
---

## Unit 1
### Lecture 3 - data science
**data science** : innovative use of data to understand something

*one or more phase should be messy - new question, new data type, unclear annotation...*

**data science project phases**: 
1. question definition
2. data collection
3. data annotation
4. data analysis
5. interpretation
6. communication

### Lecture 4 - data
**data**: collection of recorded observations

**quantitative data**: data that can be represented as numbers

**feature**: attributes (inferred) of data 

**proxies**: feature that approximates something we want to quantify (99% of time we deal with proxies)

### Lecture 5 - data collection and annotation
**data collection**: obtaining and arranging data so that we can work with it (we collect raw data, identify anomalies, correct issues, standardize data structure)

**data annotation**: applying/inferring features that will be used for analysis (can be proxy)
*generate features: human annotation, expert or corwdsourced, machine learning*

### Lecture 6 - data analysis
**data anaysis**: the creation of statistical models and visualizations using *existing* methods and *existing* clean quantitative data (existing methods on existing data to obtaun result)

**data analysts**: focused on measuring things to gain a concrete new insight. a lot of domain knowledge using analysis tools and existing things to get deeper insights

**data scientist**: focused on measuring things that have not been measured before. innovating something, the way you measure things, building new analysis tools...

### Lecture 7 - machine learning
*one of the possible solutions for when you want to measure something there isn't a measure for*

> build a mouse-hamster classifier: tail len vs body len graph. given an image it will plot and figure out what animal it is (machine that can draw more wiggly lines are more accurate but are very zone specific and expensive cost and time wise)

*ML is annotating data in data science. it needs data science: "does the ML classifier really work?" is a data science question*

### Lecture 8 - the other essential perspective
**good data science project**: your work must strive to reflect the right definition of the question. the quesiton definition must carry through. you might need to go back and refine the question (iterative process!)

*usually projects fail because questions are not asked correctly*

*just because you can think of **a** way to measure something, it doesn't mean it's the **right** way*

### Lecture 9 - good data science
*you will have to loop back in project phases - it is sus if there are no loops*

**data science projects are iterative**: because we discover our approach is broken/not doing what we intended OR our approach is wrong/working but not respecting the underlying problem

---
---

## Unit 2 
### Lecture 10 - unix
*unix is a powerful standard platform for data science*

**working with data**:
- *exploration*: initially data is unknown object
- *scale*: data can be big
- *visualization*: not initial analysis

**unix**: small modular tools that could work together:
1. write programs to do one thing well
2. write programs to work together 
3. write programs to handle text streams because it is a universal interface

### Lecture 11 - compute in the cloud
**disadvantages of laptops/desktops**:
- limited compute power
- limited special hardware and storage
- poor proximity to other ressources
- insecure
- uptime (time constraints - need to stay open)

**virtual machines**: usually next to power plants - user can grad the data for streaming very quickly

**living in the cloud**: everything is edited/run on the VPC (virtual private cloud). it has a public and private IP address

*every public computer on the internet has a public IP address*

### Lecture 12 - unix VM
**EC2 instance (lightsail)**: elastic compute

**authentication problem**: want our laptop to give instructions but nobody else. use public private keys (Kv,Kp) key pair

**EC2 - authentication problem: use SSH private-public keys**:
1. AWS account
2. SSH key pair (ssh-keygen)
3. create lightsail instance
4. `ssh -i .ssh/<instance_name> ubuntu@<IP address>`

### Lecture 13 - ssh fundamentals
**ssh**: secure shell. a way to access the unix command line on another computer

### Lecture 14 - unix command line
- `sudo (apt-get-install)`: admin rights
- `cd, pwd`: navigation
- `ls (-lna) long, human, hidden - head/tail (-n #lines) - more/less - touch (empty file) - rm - cat - mkdir - wget (download files) - mv (rename)`

*unix naming convention uses `.` instead of `_`*

*download raw files to server directly is better (right click raw file, copy link address, `wget <link>`)

### Lecture 15 - user creation
**create own user benefits**: ubuntu has elevated privileges or you might want others on the server too or its easier to SSH

**user creation**:
- `ssh <IP address> `
- `sudo adduser <username>` (same as username on computer)
- `sudo usermod -aG sudo <username>`
- `su <username>`
- `mkdir .ssh`
- `chmod 700 .ssh`
- `cd .ssh`
- *on computer* `cat ~/.ssh/id_rsa.pub` *copy it*
- `vim authorized_keys`
- *paste id_rsa.pub into the file*
- *now you can login using `ssh <IP address>`

### Lecture 16 - python installation
**python (miniconda) installation**:
- `ssh <IP address>`
- copy link address for miniconda linux online
- `wget <link>`
- `bash miniconda`
- `source ~/.bashrc` or logout and login
- confirm its the right python executable in `PATH`
- launch python interpreter

### Lecture 17 - intermediate unic CLI
**core data interrogation commands**: `ls, wc -l (# line), head, tail, grep (patterns), regex! `

**chaining commands**: `>` file redirection, `|` pipes (no files)

**env variables**: 
- `PATH` order to look in (`export -x PATH=/urs/bin: $PATH`)
- `PS1` prompt symbol (`export PS1 = $`)
- `PYTHONPATH` find python files without having to be sitting there (`export PYTONPATH=/<directory> echo $PYTHONPATH`)

### Lecture 18 - working remote
**keeping workspace alive**: so that the job running won’t get killed if you have to disconnect your computer

**tmux**: `tmux new -s <name>` OR `tmux attach -t <name>` creates a vitual computer, another workspace not connected to you computer so that when you logout the server won't kill it. it only dies when the server shuts down

**vscode**: extensions remote development `<username>@<IP address>`

### Lecture 19 - text editors
**emacs or vim**: either one is good. vim is the only editor you will ever need

### Lecture 20 - unix configuration
- `alias`: instead of typing things over and over again 
- `bashrc`: runs every login. alias only present in the current session. to make it permanent `vim .bashrc` and add commands like `aias <name> = <cmd>`
- bash scripting
- `fzf`: tool that enumerates things like creating lists. pipe things into it

---
---

### webserver
- `ssh <IP address>`
- `sudo apt update`
- `sudo apt install apache2`
- `sudo systemctl enable apache2`
- `sudo vim /etc/apache2/ports.conf `
Listen 8008
- `sudo vum /etc/apache2/sites-available/000-default.conf`
virtual host*:8008
- `sudo vim /var/www/html/comp370_hw2.txt`
Hello world
- `sudo systemctl restart apache2`
- `instance, firewall ipv4, add rule, custom, TCP, 8008`
 - `localhost:8008/comp370_hw2.txt`

### database:
- `ssh <IP address>`
- `sudo apt install mariadb-server -y`
- `sudo systemctl enable mariadb`
- `sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf`
port 6002
change bind address = 0.0.0.0
- `sudo systemctl restart mariadb`
- `sudo mysql`
- `CREATE DATABASE; `
- `CREATE USER ‘comp370’@‘%’ IDENTIFIED BY ‘$ungl@ss3s’; GRANT ALL PRIVILEGES ON comp370 * TO ‘comp370’@%’; FLUSH PRIVILEGES;`
- `instance, ipv4 firewall, add rule, custom TCP 6002`
- `sudo systemctl restart mariadb`

---
---

## Unit 3
### Lecture 21 - core tools
**core tools**:
- *exploration*: explore, messy, try things out easily, efficient, libraries
- *expressiveness*: ability to implement complex algorithms and processes
- *reproducebility*: prove that results can be obtained more than once
- *collaboration*: work together with others
- *communication*: show others/present results in engaging way, deliver prototypes

### Lecture 22 - project structure
**typical structure**:
- `<project name>`
- README.md: welcome/overview to explain goals + TODOS: notes + GOTCHAS: beware + st/installation + Running
- data
- src (source code - implements funcitonalities)
- scripts (interaction with code)

### Lecture 23 - python
**benefits**: 
- scripts = programs (explorable and tool building)
- powerful built-in data types
- data science libraries

**core libraries**: pandas dataframes, matplotlib, seaborn 

*structure - don’t forget if __name__==“__main__”: main()*

### Lecture 24 - reasons for coding
*reproduceability is very important since it proves to others thta what you did is correct*

**ways of coding**:
- *exploration*: trying things: jupyter notebook, scripts
- *tool building*: scripts, build up tools for easier use in futur, automation, packaging
- *pipelining*: big projects, automation of entire thing

### Lecture 26 - write CLI tools
**basic python script**:
```
import csv

def main():
    fname = 'file_name.csv'
    reader = csv.reader(open(fname, 'r'))
    for row in reader:
        print(row)

if __name__ == "__main__":
    main()
```

*never write a script with hardcoded params. you should be able to easily figure out what parameters your code expects and change what params values it is using*

**argparse**: for helpful messages, no hardcoding so take in arguments, should be clear what params expect
```
from argparse import ArgumentParser
import csv

def print_csv(input_file):
    reader = csv.reader(open(input_file, 'r'))
    for row in reader:
        print(row)

def main():
    parser = ArgumentParser(description="argument parser script")
    parser.add_argument("-i", "--input_file", help="input file")
    args = parser.parse_args
    print_csv(args.input_file)

if __name__=="__main__":
    main()
```

**never hardcode paths**: use os.path.dirname(__file__) to get the whole path to the file, os.path.join() to join path names in logical way

**CLI useful commands and tools**:
- `tar -xOzf file.tar.gz file.txt | grep "pattern" > result.txt`
- `csvtool -c 1 clean_dialog.csv > episode_names.csv` : looking at a specific column
- `csvtool -m 36860 episode_names.csv > episode_counts.csv`: calculates the counts of all unique values in a column and prints the top -m values with their counts. We are going to use this to find all unique values of the column, by giving a very large -m. So let's set -m to 36860 (size of the dataset), to make sure we cover all possible scenarios.
- `csvtool -c 1 clean_dialog.csv | csvtool -m 36860 | wc -l` : number of episodes. -1 for the header!
- `sort episode_names.csv > episode_names_sorted.csv` : sort the columns using `sort` 
- `uniq episode_names_sorted.csv > episode_names_uniq.csv` : remove duplicates using `uniq` 
- `csvtool -c 1 clean_dialog.csv | sort | uniq | wc -l` : count the number of unique, sorted episodes
- `csvtool -c 3 clean_dialog.csv | grep "Rarity" | wc -l` : how often a pony speaks
- `csvtool -c 3 clean_dialog.csv | grep "Rarity" | grep -v "except\|sans\|but" | wc -l` : how often without the issue of the name appearing in the except, sans, but

```
# calculate the average

import json
import sys
from argparse import ArgumentParser

def avg_calc(json_file, fieldname):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            total = sum([int(x[fieldname]) for x in data])
            avg = total/len(data)
            return avg
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)

def main():
    parser = ArgumentParser(description="average calculator")
    parser.add_argument("-i", "--input_file", help="input JSON file")
    parser.add_argument("-f", "--fieldname", help="field name to calculate average")
    args = parser.parse_args()
    avg = avg_calc(args.input_file, args.fieldname)
    print(f"average: {avg}")

if __name__=="__main__":
    main()
```

### Lecture 27 - unit tests
**unit tests**: automating testing process, prove and ensure code works after changes. quick and reproducible. testing for critical functionality

*cannot unit test in jupyter*

```
def fun_add(val1, val2):
    return val1+val2

import unittest

class Tester(unittest.TestCase):
    def test1(self):
        self.assert_Equal(fun_add(1,2), 3)
    def test2(self):
        self.assert_Equal(fun_add(-1,-1), -2)

if __name__=="__main__":
    unittest.main() 
    
# python3 -m unittest file_name.py 
```

### Lecture 28 - ressource referencing
*never use explicit paths*

**resource referencing**: ways to build paths. build paths from input arguments :
- current script location `os.path.dirname(__file__)`
- path seperators `os.path.sep`
- path combination functions `os.path.join()`

```
import os
 
def get_path():
    return os.path.join(os.path.dirname(__file__), 'data')

def get_location():
    return os.path.dirname(__file__)

def path_sep():
    return os.path.sep
```

### Lecture 29 - github
**version control**: used for collaraboration (working in teams and sharing + multi machine work replication), sharing, documentation, code backup, tracking progress

**git CLI**:
- `git clone`
- `git add`
- `git commit`
- `git push`
- `git pull`
- `.gitignore`: ignore files that should not be pushed: touch .gitignore -> add files to ignore (*.csv, *.tgz, __pycache__/, *ipynb_checkpoints)

*do not push data (large files, sensitive data)*

### Lecture 30
**jupyter notebook**: interactive, shareable, reproducible, data analysis, visualization, code, text, images. good for exploration. a notebook is a workspace/python environment that keeps a python session live. it is not good for version control

**notebook setup**:

1. install jupyter onto EC2
2. launch VSCODE
3. in terminal, launch Jupyter and note down the port number
4. in port forwarding list of VSCODE, add the port number
5. open browser and paster URL+token

*choose the right tools (jupyter vs CLI/scripts)*

*notebook will lose its state when the kernel is restarted*

### Lecture 31 - choosing the right tools
| strenghts/weaknesses | Jupyter | Scripts and CLI | 
|----------|----------|----------|
| integrated work (work + visual aids)   | + code and analysis persistently embedded in the same visual context and linear workflows are easy to capture   | - visuals separated from code and arbitrary workflows captured in scripts   | 
| state maintenance   | - easy for data and code to fall out of sync (harder maintenance) and state lost when kernel dies -> save it as csv  | + state persists in files and forced mainetance means its more organised. - state must be explicitly maintained   | 
| debugging  | - hard to unit test (only one cell running at once)   | + easy to write unit tests   | 
| long running compute  | - long jobs blocks notebook use   | + long running scripts easily kicked off in parallel and monitored | 
| collaboration  | - simultaneous editing of notebooks is tricky   | + using bersion control is easy and very smooth | 
| sharing  | + embedded documentation makes easy orientation   | + readme and source documentation for easy orientation   | 

### Lecture 32 - bokeh
*communicating results in an interactive way at the end of the project*

**Bokeh dashboard**: to cummunicate the results in live and interactive/engagin way with the client. GUI panel that allows users to view set of vizualizations in real time, configure options, and interact with the data. explore trends across variables

bokeh dashboard plots very slow, reasons: large data, complex plots, slow server
- solutions: reduce data, simplify plots, optimize server   
- data filetering, pre-computation, data aggregation, data sampling

**bokeh dashboard usage**: 
1. data preparation - get the data, filter and clean it
2. import bokeh
3. read the data, sort the options
4. create select widgets
5. create the figure (title, x_axis, y_axis) with labels
6. initialize the data source
7. plot the first set of data (.line...)
8. setup legend and layout
9. update function - callback function
10. attach the callback function to the select widgets
11. define the layout, curdoc().add_root(layout)
12. bokeh serve --port 8888 --show file_name.py

```
from bokeh import curdoc, figure
from bokeh.models import Dropdown

# prep the data
X = [x for x in range(0, 100)]
Y_up = [x for x in X]
Y_down = [-x for x in X]

# plot
f = figure(
    x_range = (min(X), max(X)),
    y_range = (min(Y_down), max(Y_up))
)
renderer = f.line(X, Y_up)
ds = renderer.data_source

# drop down menu
def select_callback(event):
    new_data = dict()
    new_data["X"]=X
    new_data["Y"] = Y_up if event.item == "y_up" else Y_down
    ds.data = new_data
    selector = Dropdown(
        label = "select", 
        menu = [("up", "y_up"), ("down", "y_down")],
    )
    selector.on_event("menu_item_click", select_callback)
curdoc().add_root(f)

# bokeh serve --port 8888 --show file_name.py
# localhost:8888 in browser
```

bokeh example from hws:
```
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Select
from bokeh.plotting import figure
import pandas as pd

df = pd.read_csv('monthly_avg_response_times.csv', parse_dates=['month'])
df['incident_zip'] = df['incident_zip'].astype(str)
zipcode_options = sorted(df['incident_zip'].unique().tolist())
zipcode1_select = Select(title="Zipcode 1", options=zipcode_options, value="10001")
zipcode2_select = Select(title="Zipcode 2", options=zipcode_options, value="10002")
p = figure(title="Monthly Response Times", x_axis_type="datetime", height=400, width=700)
p.xaxis.axis_label = "Month"
p.yaxis.axis_label = "Response Time (Hours)"

# Ensure data is sorted by month
df = df.sort_values('month')

# Initial plot for all data
all_data = df.groupby('month')['response_time_hours'].mean().reset_index()
p.line(all_data['month'], all_data['response_time_hours'], line_width=2, color='gray', legend_label="All Data")

# Plot for the first selected zipcodes
zipcode1_data = df[df['incident_zip'] == zipcode1_select.value]
zipcode2_data = df[df['incident_zip'] == zipcode2_select.value]
line_zip1 = p.line(zipcode1_data['month'], zipcode1_data['response_time_hours'], line_width=2, color='blue', legend_label=f"Zipcode {zipcode1_select.value}")
line_zip2 = p.line(zipcode2_data['month'], zipcode2_data['response_time_hours'], line_width=2, color='green', legend_label=f"Zipcode {zipcode2_select.value}")
p.legend.location = "top_left"
p.legend.label_text_font_size = '10pt'
p.legend.orientation = "horizontal"
p.add_layout(p.legend[0], 'below')
def update_plot(attr, old, new):
    # Update data for Zipcode 1
    zipcode1_data = df[df['incident_zip'] == zipcode1_select.value]
    line_zip1.data_source.data = {'x': zipcode1_data['month'], 'y': zipcode1_data['response_time_hours']}
    # Update data for Zipcode 2
    zipcode2_data = df[df['incident_zip'] == zipcode2_select.value]
    line_zip2.data_source.data = {'x': zipcode2_data['month'], 'y': zipcode2_data['response_time_hours']}
    p.legend.items = [
        ('All Data', [p.renderers[0]]),
        (f"Zipcode {zipcode1_select.value}", [line_zip1]),
        (f"Zipcode {zipcode2_select.value}", [line_zip2])
    ]

# Attach the update function to the dropdowns
zipcode1_select.on_change('value', update_plot)
zipcode2_select.on_change('value', update_plot)

# Define the layout and attach it to the document
layout = column(zipcode1_select, zipcode2_select, p)
curdoc().add_root(layout)
curdoc().title = "NYC 311 Dashboard"
```

---
---

## Unit 4
### Lecture 33 - why quesiton formulation matters
*if question formulation is wrong it will carry through the entire project*

**question format**: statement of something we want to measure (either now or a forecast)

**project phases**:
1. question formulation (what to measure)
2. data collection (how to measure)
3. data annotation (infer and add features to make measure more clear)
4. data analysis (measuring)
5. interpretation (how to understand measurements)
6. communication (how to share measurements)

### Lecture 34 - what a good question looks like
**stakeholder/use case**: person/group who asks the question (client) - *context is important*

**use case**: scenario where the system is used

**adding details/refinement**: add details to the question to make it more clear. communicate with stakeholders to get more details

> political online violence -> twitter-base. politically-active people -> non-politician politically active accounts. that self-identify as zitizens in emergung democracies -> in indonesia, columbia and kenya

> HW5 task1: the sanitary/health department wants to know where (buidings...) in the city are the more likely to have rats/mice. => cause sanitary issues -> in 202, where has there been the most sanitary complaints cased by rats/mice in the city -> in 2020, in which types of buildings has there been the most sanitary complaints where the cause was rats/mice -> in 2020 in which category of buildings (residentials, commercial, industrial) has there been the most sanitary complaints where the cause was rats/mice

> HW5 task2: the mayor wants to know if noise issues tend to stem from different causes across the year -> do the noise issue stem from different cuases across the 4 quarters of 2020 -> do the top 5 causes of noise change across the 4 quarters of 2020 -> what percentage of noise complaints due to the top 5 causes across the 4 quarters of 2020

**good question components**: detailed use case + detailed question

**process of question formulation**:
1. find a representative stakeholder
2. develop a use case (persona and concrete activity that the result of your work will use)
3. iterate on the question (ask the stakeholder for more details, look at the data, ask for more details)

*always get the client's perspective and communicate with them*

---
---

## Unit 5
### Lecture 35 - the philosophy of data science coding
*A solution is as messy as the problem and data allows it to be. data reflects the complexity of the world.*

**messy data = messy solution**

*start small, break it down, iterate, unit test, function over elegance*

*Moving through the phases of the project, it is natural at first to explore solutions and approaches. an experimental process will yield code that is not needed. the lack of alingment is messy, but it is a natural part of the process*

### Lecture 36 - modular code
*code hygiene is very important since the process is so messy*

**modularization**: breaking down the code, putting similar things together, grouped by functionality
- functions: reusable, modular, testable, readable
- classes: group functions together, more complex, more organized
- modules: group classes together, more complex, more organized
- packages: group modules together, more complex, more organized (files)

**context**: grouping depends on the objects, how similiarity is measured (how to classify might be based on available space and a number of other things)

*there is no one right way to organize code, it depends on context and how you classify things*

### Lecture 37 - redundant code (avoid)
**redundant code**: code that is repeated, nearly identical, perform nearly identical functions

**problems**: 
- hard to maintain(bugs in one block means it's also in another one)
- hard to read (need to carefully read to not miss any details)
- code bloats (more code = more to read = more to maintain)

**eliminate redundant code**: 
- recognize redundancy
- group into functions (generalize)
- break down long functions into smaller ones
- use collections (lists, dictionaries) to hold variables that are treated similarly

*it's ok to write redundant code. just make sure to recognize and tidy it up after when you do*

### Lecture 38 - dabbling
**dabbling**: trying things out, exploring, experimenting, learning

**dabbling techniques**:
1. identify sticky/critical parts
2. write just enough code to check if it is the right approach
3. try to accomplish the critical part with different tools
4. iterate on the code
5. dont get committed to the code - be ready to throw it away (learn and explore)

*approach first, tool second*

### Lecture 39 - refactor
*fastest way to becoming more adept and skilled at coding*

**refactoring**: reorganizing the structure of the code without changing the functionality

**why**: makes the code more readable, easier to maintain, easier to understand, deepens your undertanding of the code

> examples: renaming variables, breaking down long functions, grouping similar functions together, removing redundant code, changing libraries used, altering function contracts...

**when to refactor**: when you see redundancy, when you see a better way to do something, when you see a way to make the code more when we have unit tests (to be refactored as well)

**when NOT to refactor**: in the middle og adding a big piece of functionality or when you think there's a better way to do something but don't know how to do it yet

---
---

## Unit 6
### Lecture 40 - data collection
**data collection role**: collecting and preparing the raw data needed for the analysis (80% of the work), removing/cleaning the imperfections and getting it ready for analysis. 20% of the time is spent on the rest of the project

**data collection**:
1. collect the data (download, scrape, API)
2. clean the data (remove duplicates, missing values, outliers, format)
3. organize the data (format, structure, store)

**types of data**:
- *found data*: data that already exists, produced for other purposes (eg. social media, pre-existing surveys, government reports...)
- *designed data*: data generated for the purpose of the project (eg. survey, experiment results)

*the clenaing process is different for the two different types of data*
- found data: remove everything you don't need
- designed data: create data from scratch

*challenges: data too large, we don't know what the data we want looks like*

### Lecture 41 - API-based data collection
**web API**: application programmer interface with an URL that allows you to call the website and delivers raw data instead of the website. interface that allows you to interact with a web service. hit the API with a request and get a response

**public APIs**: free to use, want people to use to obtain analysis, social news displays etc. 

**web API data collection**:
1. construct URL+parameters
2. call the URL
3. receive the data
4. store the data
5. loop back to 1. if needed

*limitations: rates, authentication, available data, blacklisting, query speed, existence*

**python requests**:
```
import requests
import time
FACT_URL = "https://meowfacts.herokuapp.com/"

def fetch_fact():
    response = requests.get(FACT_URL)
    response.raise_for_status() #200 for success
    data = response.json()
    return data

def extract_fact(data):
    return data['data'][0]

if __name__=="__main__":
    with open("mew_facts.txt", 'w') as f:
        for i in range(10):
            result = extract_fact(fetch_fact())
            f.write(result)
            time.sleep(0.5)
        print(result)
```

### Lecture 42 - JSON
**JSON**: powerful data representation format, very flexible, dictionary-like, with hierarchical structure and multi-dimensional structured data

**reading JSON**: use the json library:
- `json.loads()` to load JSON from string
- `json.load()` to load JSON from a file
- `json.dumps()` to dump JSON to string
- `json.dumps()` to dump JSONto a file

*issues: not good to store large data, not human readable, not good for standarizing since it is so flexible*


```
# extracting data from json file to tsv
import json
from random import sample
import csv
import argparse 

def extract(out_file, json_file, number_posts):
    with open(json_file, 'r') as f:
        data = json.load(f)
    posts = data['data']['children']
    if number_posts > len(posts):
        selected_posts = posts
    else:
        selected_posts = sample(posts, number_posts)
    with open(out_file, 'w') as f:
        f.write("NAME\tTITLE\tCODING\n")
        for post in selected_posts:
            title = post['data']['title']
            name = post['data']['name']
            f.write(f"{name}\t{title}\t\n")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('out_file', help="output file", required=True)
    parser.add_argument('json_file', help="json file", required=True)
    parser.add_argument('number_posts', help="number of posts", required=True)
    args = parser.parse_args()
    extract(args.out_file, args.json_file, int(args.number_posts))
if __name__ == '__main__':
    main()

# plot annotations
import matplotlib.pyplot as plt
import collections
def plot_bar(tsv_file):
    annotations = {'ACADEMIC': 0, 'NEWS': 0, 'GOSSIP': 0, 'HUMOR': 0, 'OTHER': 0}
    with open(tsv_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader, None)
        for row in reader:
            annotations[row[-1]] += 1
        plt.bar(range(len(annotations)), list(annotations.values()), align='center')
        plt.xticks(range(len(annotations)), list(annotations.keys()))
        plt.show()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tsv_file', help="tsv file", required=True)
    args = parser.parse_args()
    plot_bar(args.tsv_file)
if __name__ == '__main__':
    main()
```

### Lecture 43 - reddit data collection
**reddit api**: https://www.reddit.com/dev/api/

**parameters**:
- after: fullname of a thing
- before: fullname of a thing  
- count: a positive integer (default: 0) - the number of items already seen in listing
- limit: the maximum number of items to return (default 25, max 100)
- show: optional string (all, given, hidden) - to show or hide things
- sr_detail: optional boolean value (expands subreddits)

### Lecture 44 - scraping
**scraping**: extracting data form websites without an API (no API, API is not enough, data is not available)

**HTML**: inspect browser - html hiearchy of nested tags `<tag> </tag>`. you can use beautifulsoup library to interact with the DOM and find the tag the info is sitting in

**legality**: scraping is done without permission, can be heavy on servers, not desinged for webscraping, use of data scraped

**types of scraping**:
- *static site scraping*: for pages where the whole page loads at once and all the content is already there. use `wget, curl, requests, bs4`
- *dynamic site scraping*: live pages and infinite scroll pages. the html is continuously changing. use `bs4, selenium`

*challenges: web navigation/walking, data extraction, data storage*

**scraping with cache**:
1. check if the cache exists
2. if the cache exists, use the cache
3. if the cache does not exist, scrape the page and save the cache
4. use the cache
5. soup = bs4.BeautifulSoup(html, 'html.parser')
6. find the elements (soup.find_all(), soup.find()) - using the html tags
7. extract the data and format it
8. save the data (json.dump())

```
import requests
import argparse
import os
import json
from datetime import datetime
import bs4

def get_page_caching(url, cache_loc, time_diff=60*30):
    out_html = None # no cache
    if os.path.isfile(cache_loc):
        print("Cache found for %s." % url)
        with open(cache_loc, 'r') as f:
            outdict = json.load(f) # load the cache
        last_cached = datetime.strptime(outdict['last_cached'], "%y-%m-%d %H:%M:%S")
        if (datetime.now() - last_cached).total_seconds() <= time_diff:
            out_html = outdict['html'] # use the cache
    if out_html is None: # no cache
        print("Cache not found for %s." % url)
        useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        r = requests.get(url, headers={'User-Agent': useragent}) # get the page
        out_html = r.text # get the text
        outdict = {'last_cached': datetime.strftime(datetime.now(), "%y-%m-%d %H:%M:%S"),
                   'html': out_html} # cache the page
        with open(cache_loc, 'w') as f:
            json.dump(outdict, f) # save the cache
    return out_html

def get_cache_hash(title, hashfile):
    with open(hashfile, 'r') as f: # load the hashlist
        hashlist = json.load(f)
    if title in hashlist: # if the title is in the hashlist
        return hashlist[title]
    new_index = max(hashlist.values())+1 if len(hashlist.items()) > 0 else 0 # get the new index
    hashlist[title] = new_index # add the title to the hashlist
    with open(hashfile, 'w') as f: # save the hashlist
        json.dump(hashlist, f) 
    return new_index

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", required=True, type=str, help='Output file')
    args = parser.parse_args()
    BASE_URL = 'https://montrealgazette.com'
    homepage_text = get_page_caching(BASE_URL + '/category/news/', 'cache_files/homepage.json')
    soup = bs4.BeautifulSoup(homepage_text, 'html.parser') # parse the page
    trending_div = soup.find('div', class_='col-xs-12 top-trending')
    trending_stories = trending_div.find_all('a', class_='article-card__link')
    ts_links = [BASE_URL + ele['href'] for ele in trending_stories]
    story_details = []
    for story in trending_stories:
        hashindex = get_cache_hash(story['aria-label'], 'cache_files/hash_list.json')
        story_text = get_page_caching(BASE_URL + story['href'], f'cache_files/%d.json % hashindex')
        soup = bs4.BeautifulSoup(story_text, 'html.parser')
        title = soup.find("h1", class_="article-title").text
        publication_date = soup.find("span", class_="published-date__since").text
        author_object = soup.find("span", class_="published-by__author")
        if author_object is None:
            author = "Montreal Gazette"
        else:
            author = author.find('a').text
        blurb = soup.find("p", class_="article-subtitle").text
        story_details.append({'title': title, 'publication_date': publication_date, 'author': author, 'blurb': blurb})
    with open(args.outputfile, 'w') as f:
        json.dump(story_details, f)

if __name__=="__main__":
    main()
```

### Lecture 45 - sampling and bias
**sample**: a subset of the data you want

**sampling**: taking a subset of the data, more manageable (large data files), easier to define and understand, faster to process

> how many friends do Twitter users have - hard to obtain the info

> % news articles that mention Marvel - no API for all news coverage + "mention Marvel"? + all news is a lot

> how many bots posted to Reddit - how to identitfy bots?

**types of sampling**:
- *systematic sampling by ID*: each object has an ID, walk through and grab every few
- *snowball sampling*: starting with an object, pick up the neighbours (very biased towards the first entity needs pruning)

**bias**: disproportionately weight factors that impact measurements. bias can be good

*everything is biased and it's not necessarily bad if we are aware of it and don't just ignore it*

**handling bias**: 
- "what are the biases"
- "comfortable with the biases"
- "engage with biases we want to keep"
- "eliminate others"

**paradox of the sample design**: sample X to learn more about it <=> to sample properly we need to know more about X

*spend time studying the data, think of the blind spots and engage with them -> iterate and educate yourslf. gather what you can knowing it is biased, characterize it and look/engage with another community and repeat*

---
---

## Unit 7
### Lecture 46 - annotation and typology
**annotation**: adding features to the data that will be important to the analysis. assigning properties that are not reliably self-reported

*what to focus on, standardize labels, conceptual coherance/agreement*

**goal**: accurately and reproducibly assign labels to a set of data objects

**annotation tasks**:
1. devising the labels to use
2. assigning the labels to the data

**types of properties**: 
- Real-valued 
- Categorical (classifications)

**typology**: a comprehensive (any object in the space will fit in one or more types), sharphy defined (each type has a definition that allows systemic evaluation of whether an object is of that type - threshold is important) categorization system. *(objective-ish: definitions should strive to be as objective as possible - if not possible use strategies to make subjective categories more objective: have the same frame to interprete something)*

**forced choice**: there is no right label, but forcing the annotator to pick something

*any categorical property requires a typology (some things are harder than they seem - hard to define labels, hard to dissern with available info)*

### Lecture 47 - building a typology
**typology design objective**: a document consisting of motivation (why typology exists) and contect, overview of types and relation to one another, list of types (with concise definitions, positive examples with inlusion rational, negative examples with exclusion rational, edge cases with inclusion and exclusion rational), arguments/evidence for comprehensivness -> human readable, intended for humans document that lays out the purpose and category of typology, and defines the types of categories including data examples, outide cases and edge cases

**building a typology**:
1. Get representative data
2. Get typology (existing or build own using open coding)
3. Sanity check: evaluate typology on representative data yourself
4. Human test: use "expert" coders to evaluate typology on representative data (make sure it is generalizable and unambiguous)
5. Does it work? (if not, go back to step 2. if so, move on)

**open coding**: take sample of data and code it, then look for patterns and create categories, review and iterate

**typology has to be**:
- *comprehensive*: all data should fit into one or more categories. **do not** have a catch all others category - it can lead to confusions
- *sharply defined*: each category should have a clear definition that allows for systematic evaluation of whether an object is of that type. make sure to know where the ambigous cases are
- *objective-ish*: definitions should strive to be as objective as possible. if not possible, use strategies to make subjective categories more objective

*building typology is iterative process, long and hard. requires a lot of data and a lot of thinking*

### Lecture 48 - human coding
**human coding**: the process of assigning labels to data objects. 

**approaches**:
1. Expert coding: people very trained for the task (you, colleagues, small gruop of trained participants, hired experts)
2. Crowdsourcing: using a large group of non-experts to code data (Amazon Mechanical Turk, CrowdFlower, etc.)

**ethics approval**: capacity for harm. research proposals should be reviewed by an ethics board to ensure that the research is ethical. (are there potential harms? are they justified? are there ways to mitigate them?)
1. disclosing damaging information can harm the participants/research subjects
2. harm to the annotators (mental health, privacy, etc.)

**training**: help coders understand the concepts and how to apply them on a deeper level + refine the typology
1. prepare a code book (typology definition document)
2. provide examples (challenging)
3. run the group sessions (with time to explain and discuss)

**human coding process**: *loops and iterations are common*
1. preparation phase: decide on group, develop code book/training material/examples, develop annotation software or put into format people can use
2. annotation phase: recruit coders, run training sessions, have coders code data
3. validation phase: thoughout, assess quality and level of agreement among coders -> if low, retrain coders or refine typology, else you have a good typology

### Lecture 49 - confirming annotation quality
**perfect agreement**: all coders agree on all labels

**majority agreement**: most coders agree on most labels. usually go with majority label as the final label

**no majority agreement/no agreement**: check it youserlf, decide on the label, or refine the typology

*look at the % of each type of agreement, might need to retrain coders or refine typology -> do this in annotation phase to save time*

**interpreting annotator agreement**:
- confusing typology: confusion between labels -> refine typology
- bad coder: one coder is not doing well -> retrain or replace
- tricky cases: confusion on edge cases -> refine typology, define new edge cases
- human error: occasional errors -> go over the data and correct

### Lecture 50 - automated annotation
**automated annotation**: using algorithms to assign labels to data objects. (CSV -> algorithm -> labeled data)

**where to use automated annotation**:
1. when there is an established automated annotator you can use directly (hard to find)
2. when it is part of research project to develop an automated annotator

### Lecture 51 - giving precise answers
**precise answer**: a statement that provides all the details the audience requires in order to use the information in a wide array of contexts 

*identify the audience, what they need to know, and how they will use the information*

*examples are not precise answers -> does not cover a wide array of contexts*

**factors to determine answer**:
1. the question objective
    1. what = a definition
    2. how = an explanation/a process
    3. why = an explanation of motivation
2. level of detail expected by the audience

> blender example: **what** is a blender? **how** does a blender work? **how** do we use a blender? **why** does a blender work? **why** do we use a blender?

---
---

## Unit 8
### Lecture 52 - what is analysis
**analysis**: the process of breaking a complex topic or substance into smaller parts in order to gain a better understanding of it

**substantiating insights**: data analysis is to back up our insights. the goal is to get smaller pieces to back up our insights

**asnwering questions**: select/build a tool, prepare data, apply tool to data, sanity check results

**follow up**: is answer obvious? would answer impact validity/relevance of result we have insight sought?

**fishing expedition**: 
when you don't have a question and you are just looking at the data to see what you can find. (are there any? what are the factors?)
- ask questions that narrow the open ended question to bound question
- analysis should have a concrete outcome/insight in mind. if no target insight, you are fishing for interesting things
- results attempt to support insight 

### Lecture 53 - what is a result
**result**: a claim that can be directly verified using a process and data

**valid result**: data must be valid + method must be valid

**data/method dependency**: data and method are dependent on each other. if you change one, you have to change the other

### Lecture 54 - most frequent world analysis
**TF-IDF**: term frequency inverse document frequency. a term's overall score should be impacted by how common it is in general. *for analysing text*

> `tf-idf(term, document, Documents) = tf(term, document) * idf(term, Documents)` -> frequency of the term in the category * the penalty term

> `idf(term, Documents) = log(total_num_catgories / (|{document in Docments: term in document}|))` -> log of the total number of categories divided by the number of categories that use the term

**stopwords**: get rid of filler/stop words before doing the tf-idf analysis (words like "a", "the", "and" ...)

> example (each pony's most frequently used words): TS: friend * 10, party * 5, spell * 5. PP: friend * 10, -. R: friend * 10, -, -.  AJ: friend * 10, -, -. RD: friend * 10, -, -. FS: friend * 10, -, -.

> "friends": tf("friend", TS) = 10. idf("friend", P) = log (6/6) = log(1). tf-idf("friend", TS, P) = 10 * 0 = 0

> "party": tf=5, idf=log(6/2), tf-idf = 5 * log(3) = 2.4

> "spell": tf=5, idf=log(6/1), tf-idf = 5 * log(6) = 3.9

```
import argparse
import json
from collections import Counter, defaultdict
import math

def load_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords = [line.rstrip() for line in f]
    return stopwords

def extract_titles(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    posts = data['data']['children']
    titles = [post['data']['title'] for post in posts]
    return titles

def tokenize(titles):
    tokenized_words = []
    for title in titles:
        words = title.split(" ")
        words_filtered = [word.lower() for word in words if word.isalnum()]
        tokenized_words.extend(words_filtered)
    return tokenized_words

def term_frequencies(tokenized_words):
    tf = Counter(tokenized_words)
    return tf

def inverse_document_frequencies(all_filtered_words):
    num_documents = len(all_filtered_words)
    idf = defaultdict(int)
    for filtered_words in all_filtered_words:
        unique_words = set(filtered_words)
        for word in unique_words:
            idf[word] += 1
    idf_scores = {word: math.log(num_documents / count) for word, count in idf.items()}
    return idf_scores

def remove_stopwords(tokenized_words, stopwords):
    filtered_words = [word for word in tokenized_words if word not in stopwords]
    return filtered_words

def tfidf_scores(filtered_words, idf_scores):
    tf_scores = term_frequencies(filtered_words)
    tfidf_scores = {word: tf_scores[word]*idf_scores[word] for word in tf_scores}
    return tfidf_scores

def tfidf_word_list(out_file, word_lists, stop_word_file):
    stopwords = []
    if stop_word_file is not None:
        stopwords = load_stopwords(stop_word_file)
    all_filtered_words = []
    for word_list in word_lists:
        titles = extract_titles(word_list)
        tokenized_words = tokenize(titles)
        filtered_words = remove_stopwords(tokenized_words, stopwords)
        all_filtered_words.append(filtered_words)
    idf_scores = inverse_document_frequencies(all_filtered_words)
    word_counts = {}
    for word_list, filtered_words in zip(word_lists, all_filtered_words):
        word_scores = tfidf_scores(filtered_words, idf_scores)
        sorted_scores = sorted(word_scores.items(), key=lambda x: -x[1])
        word_counts[word_list] = sorted_scores[:10]
    with open(out_file, 'w') as f:
        json.dump(word_counts, f)

def main():
    parser = argparse.ArgumentParser(description='TF-IDF word list.')
    parser.add_argument('-o', dest='out_file', required=True, help='Output JSON file')
    parser.add_argument('-s', dest='stop_word_file', help='Stop words file')
    parser.add_argument('word_lists', nargs='+', help='INput JSON files')
    args = parser.parse_args()
    tfidf_word_list(args.out_file, args.word_lists, args.stop_word_file)

if __name__=="__main__":
    main()
```

### Lecture 55 - network analysis
*networks look at the spread of disease/information, looking at the major nodes and connectivity (instead of euclidian distance)*

**network terms**:
- *node (vertex)*: entity
- *edge*: relationship
- *path*: sequence of adjacent edges
- *weights*: strenght of edges

### Lecture 56 - working with network data
**networks**: are everywhere. objects that have distinct connections to one another. *central idea* is that nodes with relationships behind them and the *power* is that it can capture the relationship behind nodes and their structure

**directed network**: edges have direction and cannot flow backwards (eg. flows/transportation/process/twitter) * -> *

**undirected networks**: info can flow in both directions or we only care about the structure * - *

**building a network**: we need transactions (since they contain relationships implicitly) data
- node attributes (eg. characteristics of a person)
- edge direction (eg. who initiated the convo OR a convo happened - undirected)
- edge weight that represents the strenght of a transaction (eg. lenght, importance)

> examples: social media networks, protein networks, character interaction networks, road networks ...

> social media networks: nodes (different accounts), edges (following/friends OR blocking OR liking/commenting interactions OR messaging OR tags/mentions), weights (mentions # of times, can be directional), data (posts data, query account metadata -> API or scraping)

> protein networks: nodes (proteins), edges (interactions binding reactions), data (mod proteins to change something about it, microarrays/test tubes with proteins, experiments ...)

> character interaction networks: nodes (characters), edges (talking, mentions, co-appearance, physical, interactions), data (scripts, video frames ...)

> road networks: nodes (cities/towns, intersections), edges (roads), weights (distance, traffic - #cars with average speed), data (GIS maps, live annotations from other users)

**network representation**: edge lists (csv with 2-3 columns): nodes with edges (rows) (eg. char1, char2, #)

**libraries for networks**: networkX

### Lecture 57 - network structure analysis
**when connectivity matters**: the whole is greater than the sum of its parts - use networks!

**scales of network analysis**:
```
<--------------------------------------------------------------------------------------------->
individual           neighbours             communities                   whole system
(not too much        (connected to)         (larger groups,              (network as a whole)
transactions)                               might have an attribute)

          microscale               mesoscale                    macroscale
```
> eg. info spread: *individual* (do people have many friends), *neighbours* (which people are liekly to hear it first?), *communities* (are people grouped together in tight-knit comminities?), *whole system* (how similar is spread of info to spread of another info?)

**centrality**: who controls the spread. how important a person is in the network

**degree**: most central nodes -> calculate degree of all nodes and take the one with highest degree

**closeness**: number of hops to get to every other node in the system

**betweeness**: b(v)=fraction of all shortest paths in the network that pass through v (how important. if removed it will cut the connection of the graph) - essentialness 

**communities/clusterings**: community module is how to group nodes. *percolation technique* (removing edges until you get your module)
- modularity detection: want a small number of crossing edges relative to the number of edges in the cluster
- modularity: the ratio of the number of edges inside the cluster vs. outside

> TODO: examples from hw12

---
---

## Unit 9
### Lecture 58 - interpretation
**communication == persuasion**: in data science, aim to use evidence to convince someone our answer to the original question is correct. *evidence is not an argument*, assemble the argument using the evidence. *interpretation* is the beginning of communication (how to give back to the stakeholders)

*introducing new evidence is the analysis phase, not interpretation*

**evidence != answer**:
- a result provides a very specific detail about answer. question is multidimensional
- result meanings depends on method (data used)
- result don't go all the way to the answer, you need to convince the audience that the proxy is good enough
- hard to present and organize

**interpretation**: using evidence to support a conclusion. separate presenting evidence and intrepretation, it connects evidence to the conclusion, making an argument to the audience as to why they should "believe"

**structure**:
- restate the original question...
- key big point # + takeaways with evidence to validate it
- concluding section draws on main points (not directly on the evidence)

*analysis will establish the validity of the evidence and interpretation can use these + present the methods that got us here*

**technique to get the big key points**:
1. assert contextualization (yes/no answers are very rare, focus on points with evidence support)
2. include negative outcomes (100% success are sus - need to build confidance)
3. support by combining results + extrapolating from results (most points require combining results and when a result can't get all the way, argue that it points in the right direction)
4. use points to make a meta point (build based on findings instead of eveidence) -> something that ties all into a single answer (conclusion)

*if conclusion is just a big point it is not a conclusion*

**approach to interpretation**:
1. write out big points that stand out after analysis
2. decide on a rough conclusion that fits the big points
3. write out arguments for each point
4. if arguments need more evidence, loop back to the analysis. else if the evidence supports a differnt point loop back to 1.
5. refine the conclusion

### Lecture 59 - communication
**persuasion/story**: research project is a story. *value*: stories are compelling because they introduce and then resolve tension. stories enhance understanding and capture how each event is connected to the next

**audience**: remember the audience, what you emphasize and how you explain will differ

### Lecture 60 - visualization
**principles**: every visualization has a purpose in the storytelling. looking at a visualization, you should be able to say what the purpose is. every detail should contribute to that purpose. design elements should appeal to the udience intuition and require minimal explanation

> word clouds are bad visualizations! use a bar plot / pie chart / lists / historgram ... depending on the purpose

**necessary details**:
1. readable visualization: no bad resolution, right size/dimension
2. title: state the purpose (all tables/plots)
3. caption: block of text not too long attached, explaining how to read and understand the plot. indicate what to see and what to notice (persuasion!)

**audience consideration**: what is intuitive to your audience, how is it consumed (online/printed/colours), perceptual contraints

### Lecture 61 - written reports
**technical report structure** (like a heist movie):
- *motivation*: why are we here, the reasons, what things mean
- *objective/problem*: what is the problem
- *data* (the data can also be after, part of the results)
- *design/methods*: preparation, how to understand what the rest of the report is talking about, how we got the data, everything fundamentally affecting the results
- *results*: we did this explained in the methods and we got this as a result here
- *findings/interpretation/discussion*: no more results, what everything means and piecing things together
- *conclusion*: the bigger picture, only understood by someone who has been on the whole journey, what it really means. why do we care/why we did the study, what's next (future work)

**visualizations and tables**: must be used by the text to have a point unless paired with a caption, then it should make sense on their own as well

**technical != boring**: technical language is precise and favours quantitative details but it can also have personality! good style (active voice - "we found", bridging sentences for flow). it can tell a story

### Lecture 62 - presentations
*make a good impression on the stakeholders*

**presentation is a story**: data science project is a journey where you return with a treasure. the presentation is where you tell the story and share the treasure

**slides**: are optional and a good presentation shouldn't require them. they are good to help visualize but you should be able to talk about everything without them. they help emphasize important things and provide details that are harder to describe

**structure**:
- relatable opening (stories, personal experiences, why you care etc.)
- motivation
- objective/problem
- date
- design/methods
- results
- findings/interpretation/discussion
- conclusion

*assume the audience will only take one thing away, so focus on that. take every chance to highlight the motivation throughtout the presentation for example*

*practice and anitcipate questions + put yourself in the story, your experiences. make it engaging!*

---
---

## Unit 10
### Lecture 63 - data scientist
- nobody knowns all the tools. being a data scientist is about having a conceptual framework for using messy data to learn about the world + having the foundation skills to identitfy and build methods + having an interest to continue developing abilities
- lots of career options: *data science savvy organisations* (join a team), *data science noob organisations* (make a team), *data science resistant organisations* 

*learn as you go and adapt*

### Lecture 64 - data science skills
- keep learning. data science is a rapidly evolving field
- **learn**: 
    - modelling (stats/machine learning)
    - data engineering (database/data munging)
    - high performance compute (distributed/streams)
    - software development
    - specific domain knowledge
    - communication
- *learning != mastering*. use it at least once, play around with it and try things out. make personal projects or take classes!

### Lecture 65 - social networking
- develop and maintain a professional network
    - how: attend meetups, conferences, workshops, clubs, open source projects, tutorials etc.

### Lecture 66 - landing a job
- don't get discouraged, rejections are part of the process






---
---
---

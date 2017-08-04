# Guidelines and quality metrics for programming code developed within the DD-DeCaF project

<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. Introduction</a></li>
<li><a href="#orgheadline7">2. Characteristics of good software</a>
<ul>
<li><a href="#orgheadline2">2.1. Tidy, readable and well organized</a></li>
<li><a href="#orgheadline3">2.2. Appropriately documented</a></li>
<li><a href="#orgheadline4">2.3. Verifiable</a></li>
<li><a href="#orgheadline5">2.4. Readily available and easy to install</a></li>
<li><a href="#orgheadline6">2.5. Clearly licensed</a></li>
</ul>
</li>
<li><a href="#orgheadline8">3. Template</a></li>
</ul>
</div>
</div>


# Introduction<a id="orgheadline1"></a>

When it comes to the question of *software quality* in computational biology it is useful to make a distinction between *programmatic data analysis* and *software development*. The first is the process of writing instructions for a computer to analyze a given dataset and produce the desired result. The focus on a single task allows the researcher to progress relatively fast and to do little additional work than working out the biological and mathematical/statistical theory. Numerous great algorithms, methods and models have been implemented this way with corresponding rapid insights. Software development on the other hand, is the process of creating a tool that can reliably be used by someone else than the original author to perform that analysis for a different dataset, using a different computer and without direct communication with the original developer. 

The importance of achieving results that are not only novel and exciting but also usable by other researchers have been highlighted by [recent difficulties](http://science.sciencemag.org/content/334/6060/1226) to reproduce many published findings in general and to apply them to new datasets in particular. As a reaction to this, [good practice](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002802) for [scientific software development](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745) have been forth and thanks to readily available tools to aid software engineering there are now few reasons for not writing software that is understandable and that works well.

In the DD-DeCaF project, we aim to make state-of-the-art algorithms, models and visualization techniques readily available not only to ourselves but also to the community in general and for this to be possible it is essential that we adhere to a minimum of good software development practice. Here, we highlight the most central aspects of such practice and make recommendations for how to adopt these when developing in our main language of choice for scientific computing - python.

# Characteristics of good software<a id="orgheadline7"></a>

## Tidy, readable and well organized<a id="orgheadline2"></a>

Although we write code for it to be executed by a computer, it is essential that is also understandable by humans as it must be possible to read and understand if one is to be able to collaborate, verify and extend the software. When writing texts in natural language, we must pay attention to rules for punctuation, space and capitals &#x2013; computer languages are no different. Good software should have a consistent (1) *coding style*.

Furthermore, as software typically consists of a large set of components that inter-operate it is critical that these are well organized and easy to find. Just as a lab must have its regents and tools neatly organized, the parts of a software project must also be kept in good order - particularly since these parts change over the course of the project. The use of (2) *version control* is essential.

## Appropriately documented<a id="orgheadline3"></a>

For other developers and users alike, it is typically necessary that the software comes with documentation for how it works, what all the parts of the software does and how one should use it. Good (3) *documentation* is up-to-date, concise, understandable and sufficient.

## Verifiable<a id="orgheadline4"></a>

For anything but a very small software project, it is impossible to manually keep track of all the functions, what they actually do and how they may be affected when changing a perhaps seemingly unrelated part of the program. In order for the released software to really do what the developer originally intended, we must write additional software that specifically aims to test functionality and to report if (when) something breaks. Such tests are called (4) *unit tests* and ideally the entire project should be subject to at least one of these tests leading to what is called 100% (5) *coverage*. 

## Readily available and easy to install<a id="orgheadline5"></a>

The software is of course only useful to someone else if that person can access it. If the software needs to be installed locally, this process should be possible on all combinations of targeted operating systems and necessary dependencies. To ensure that this really is the case it is important to use tools for that (6) *continuously integrates new changes, tests and deploys* the software.

## Clearly licensed<a id="orgheadline6"></a>

All software, whether stated or not, comes with copyright and terms for usage, modification and distribution. Different organizations and monetization models have different requirements but in either case it is important that the conditions are clearly stated by the (7) inclusion of a text file that details these.

# Template<a id="orgheadline8"></a>

The last few years has seen the emergence of widely available software engineering tools, often provided free of charge, that greatly facilitates writing high quality software. However, since the number of available tools is quite large, and configuring them for your own project can be a hurdle, we recommend using templates that can be used to rapidly initialize a new project.

One such templating tool is [**cookiecutter**](https://github.com/audreyr/cookiecutter) which can create software templates for any programming language given the corresponding template. In order to simplify the creation of new python packages in the DD-DeCaF project, we created the **cookiecutter-decaf-python** template which by answering a few questions from the user rapidly can setup new python projects that:

1.  Is automatically checked for consistent coding style using the
    [**flake8 tool**](http://flake8.pycqa.org/en/latest/) which implements the standard
    guidelines called [PEP8](https://www.python.org/dev/peps/pep-0008/).
2.  Uses [**pydocstyle**](https://github.com/PyCQA/pydocstyle) to check that documentation is available and
    correctly formatted for rendering on websites such as
    [**readthedocs.org**](https://readthedocs.org/)
3.  Uses **git** and GitHub for version control and easy collaboration with
    other developers.
4.  Uses [**pytest**](http://docs.pytest.org/en/latest/) for writing unit-test
5.  [**codecov.io**](https://codecov.io) to check how much of the
    code is being addressed by those tests.
6.  Uses [**Travis**](https://travis-ci.org/) for continuous integration /
    testing on Linux and [**AppVeyor**](https://ci.appveyor.com/) for Windows.
7.  Has an explicit license file included in the package.

Starting a new python package can be done by at a shell issuing

    pip install cookiecutter
    cookiecutter gh:dd-decaf/cookiecutter-decaf-python

and answering the questions that are asked at the prompt. After that, go to the various mentioned websites and in most cases you simply have to login using your GitHub account and enable the desired service - your project already has the necessary configuration files.

Taken together, the adherence to the principles above, jointly make up a static code quality metric that indicates how healthy the current code base is - our aim is that all software written in DD-DeCaF both implements great features and score well on these metrics to ensure long term operability and sustainability.

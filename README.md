# Morse code + Audio
This is an python program that **Encode Text to Morse code**, **Decode Morse code to Text** and  
there is an option to listen to ***Audio* of Morse code**  


![morse codes](https://media.geeksforgeeks.org/wp-content/uploads/20231228095556/morse-code_2.jpg)


## 1. Project Setup

+ Clone this repository using git:
   
```bash
    git clone https://github.com/ASoukhteh/Morse-Code.git
```
## 2. Setup the environment
+ Setup the build environment for your target operating system:

### Mac

+ Install the xcode command line tools if you don't already have them installed:
```bash
    xcode-select --install
```
### Ubuntu

+ Install the following developer libraries using apt-get:
```bash
    sudo apt-get install -y python3-dev libasound2-dev
```
### CentOS
 
+ Install the following developer libraries using yum:
```bash
    sudo yum install alsa-lib-devel
```
## 3. Python Depedencies

+ Create virtual environment:

```bash
    python -m venv env
```
### Activate virtual environment
+ Mac/Linux
```bash
    source env/bin/activate
```
+ Windows and other
<div class="responsive-table__container"><table class="docutils align-default">
<thead>
<tr class="row-odd"><th class="head"><p>Platform</p></th>
<th class="head"><p>Shell</p></th>
<th class="head"><p>Command to activate virtual environment</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="4"><p>POSIX</p></td>
<td><p>bash/zsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>fish</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate.fish</span></code></p></td>
</tr>
<tr class="row-even"><td><p>csh/tcsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate.csh</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>pwsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/Activate.ps1</span></code></p></td>
</tr>
<tr class="row-even"><td rowspan="2"><p>Windows</p></td>
<td><p>cmd.exe</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">C:\&gt;</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">\Scripts\activate.bat</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>PowerShell</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">PS</span> <span class="pre">C:\&gt;</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">\Scripts\Activate.ps1</span></code></p></td>
</tr>
</tbody>
</table></div>

+ Install the following python modules into your virtual environment using PIP:

```bash
pip install -r requirements.txt
```

+ Test that the install of **simpleaudio** was successful, open a python intrepreter by typing `python` in your virtual environment console. In the python intrepreter, type the following commands:

```python
import simpleaudio.functionchecks as fc
fc.LeftRightCheck.run()
```

```text
You should here a piano note from each of your computer speakers.
```

----

I inspired by and use this [repo](https://github.com/jbourquin/morse-code) to add audio to my codes.


<div align="center">
    <h1>Particle Life</h1><h5> An A.I. simulation of particles 🎇</h5>
    <img src="https://img.shields.io/github/stars/Shreejan-35/Particle-life?style=for-the-badge"></img> <img src="https://img.shields.io/readthedocs/pip?style=for-the-badge"></img> <img src="https://img.shields.io/maintenance/yes/2022?style=for-the-badge"></img> <img src="https://img.shields.io/github/license/Shreejan-35/Particle-life?style=for-the-badge"></img>
</div>


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#documentation">Documentation</a>
      <ul>
        <li><a href="#libraries">Libraries</a></li>
		<li><a href="#code-explanation">Code Explanation</a></li>
		<li><a href="#rendering-particles">Rendering Particles</a></li>
	        <li><a href="#main-rules">Main Rules</a></li>
		<li><a href="#simulation">Simulation</a></li>
      </ul>
    </li>
    <li><a href="#examplestests">Examples/Tests</a>
	</li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#support">Support</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Documentation

Particle Life is just a simple python script.
It makes a window and shows different movement of particles,
whose rules are defined by us while writing the code. It is a simple
python script in which I have implemented OOP.

### Libraries

The python libraries that are used are :-

- pygame

  - `pip3 install pygame`

- math
- random

### Code explanation

- A `Particle` class is there which takes -
  - true for running the while loop
  - width of screen
  - height of screen
  - color of screen in rgb in this case - `rgb(0,0,0)`
- `createParticle` function - This renders a particle in the screen with specific color and coordinates
- `returnParticle` function - Returns a dict consisting of x,y,color,velocityX,velocityY
- `manyParticles` function - Returns a list of particles consisting of the above dictionary with random x and y positions
- `createParticles` function - Creates all the particles in the list returned above using the `createParticle` function
- `mainRule` function - Uses physics and maths formula to attract the particles towards each other and reflect back the particles by using the value of `g`
  - Formula Used:-
    - F = GMm/r^2
    - squareroot[(x2-x1)^2 + (y2-y1)^2]
    - F = ma
  - Important things -
    - g is -ve if the particles are attracted
    - g is +ve if the particles are repelling each other

### Rendering Particles
- To render particles two things we need to run -

  - `self.yellowParticles = self.manyParticles(200, self.yellow)` - To get the list of particles
  - `self.createParticles(self.yellowParticles)` - To render the particles, used in the while loop
  
### Main Rules
- To write the mainrules, we need to give 3 arguements - particles list1, particle list2, g
  - `self.mainRule(self.yellowParticles, self.yellowParticles, -0.1)` - Here yellow particles are attracted by each other by a small force of 0.1

### Simulation

You can simulate the particle animation by writing the mainrule, rendering particles and defining colors.

- Define colors

  - `self.yellow = (255, 255, 0)` - It should be written in `def __init__`

- About Rendering particles you can get the information above
- Write your mainrules as you want in the while loop

## Examples/Tests
*This are some of the tests that are done.*

|                                                                                                                                                    First Test Case                                                                                                                                                     |                                                                                                                                                                                                             Second Test Case                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Third Test Case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                     ![](https://github.com/Shreejan-35/Particle-life/blob/master/images/first.gif)                                                                                                                     |                                                                                                                                                                              ![](https://github.com/Shreejan-35/Particle-life/blob/master/images/second.gif)                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ![](https://github.com/Shreejan-35/Particle-life/blob/master/images/third.gif)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `self.mainRule(self.redParticles, self.redParticles, -0.1) self.mainRule(self.yellowParticles, self.redParticles, 0.01) self.mainRule(self.redParticles, self.yellowParticles, -0.01) self.mainRule(self.yellowParticles, self.yellowParticles, -0.1) self.mainRule(self.yellowParticles, self.yellowParticles, 0.01)` | `self.mainRule(self.redParticles, self.redParticles, 0.1) self.mainRule(self.yellowParticles, self.redParticles, -0.12) self.mainRule(self.greenParticles, self.greenParticles, -0.7) self.mainRule(self.greenParticles, self.redParticles, -0.2) self.mainRule(self.redParticles, self.greenParticles, -0.1) self.mainRule(self.greenParticles, self.greenParticles, 0.10) self.mainRule(self.redParticles, self.yellowParticles, 0.09)` | `self.mainRule(self.yellowParticles, self.yellowParticles, 0.1) self.mainRule(self.blueParticles, self.blueParticles, 0.1) self.mainRule(self.blueParticles, self.yellowParticles, -0.12) self.mainRule(self.yellowParticles, self.blueParticles, 0.01) self.mainRule(self.yellowParticles, self.greenParticles, 0.1) self.mainRule(self.blueParticles, self.greenParticles, -0.23) self.mainRule(self.blueParticles, self.redParticles, -0.2) self.mainRule(self.redParticles, self.blueParticles, -0.1) self.mainRule(self.greenParticles, self.blueParticles, 0.12) self.mainRule(self.redParticles, self.redParticles, 0.1) self.mainRule(self.yellowParticles, self.redParticles, -0.12) self.mainRule(self.greenParticles, self.greenParticles, -0.7) self.mainRule(self.greenParticles, self.redParticles, -0.2) self.mainRule(self.redParticles, self.greenParticles, -0.1) self.mainRule(self.greenParticles, self.yellowParticles, 0.13) self.mainRule(self.greenParticles, self.greenParticles, 0.10) self.mainRule(self.redParticles, self.yellowParticles, 0.09) self.mainRule(self.yellowParticles, self.redParticles, -0.2)` |

## Installation

The Installation is pretty easy.

- Make a directory in your computer to store the files.
- Go into the directory and clone the git repository

```
git clone https://github.com/Shreejan-35/Particle-life.git
```

- Open your favourite terminal, and type this commands

```
pip3 install requirements.txt
```

Then,

```
python3 particle.py
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b any-name`)
3. Commit your Changes (`git commit -m 'Add some advices'`)
4. Push to the Branch (`git push origin`)
5. Open a Pull Request

## Support
Support me by following me and giving a ✨ to this repo.

## License

MIT LICENSE

# The Collection
The Collection is a site, which allows a registered user to create and easily manage collections of his beloved items.

The application satisfies the demand for a simple solution, to easily inventory individual things in a beautifully designed cataloge. This can be, for example, a collection of weapons, a collection of model cars or very practical things, such as spare parts for motorcycles. Everything is possible!

A Collection consists of multiple individual items, where each item can be described and images can be uploaded to make the catalog more appealing.
A search function gives the user the possibility to find the item of his desire inside a collection.
    
Link to deployed site: [The Collection](https://the-collection-rpf13.herokuapp.com/)

![Mockup](docs/images/106-2_techsini_rsponsive.png)

---

## User Stories

### EPIC - XYZ


---

## UX & Design

The overall design has been kept very simple, kind of industrial design and raw. The main focus should be the content, which is the uploaded image and the description. Everything else should be in the background. Therefore the whole colore scheme is dark, to give the focus to the content - either via the cards containing collections or the item list. The background of the descriptive description inside the card is intentionally white, in order to have immediate focus.

The design is minimalistic, the navigation very intuitive. The background animation is subtile, it does not distract but gives a nice colorful effect, evne though it is kept dark. The main heading of the entry site is an eye catcher, with its transparent text and the moving, dark colored clouds behind it.

---

### Color Scheme

There are different color sets used in this project. Furthermore, the Bootstrap included colors / color classes have been used. I have used [Coolors](https://coolors.co/) to pick and compare the various colors.
I have spent quite some efforts to make sure, all colors and color combinations pass the contrast test, making sure the accessibility is given.
The main font color palete contains the following colors: #F5F5F5 is used as text color, in addition the Bootstrap "text-light" (#F8F9FA). The #C0C0C0 has been used as a replacement for the standard "blue" active link color, in order to give a better contrast on the background. The #343A40 is the standard Bootstrap black. The red, blue and purple colors have been used to highlight the social media fonts, when hovering.

<details>
<summary>Font Colors</summary>

![Font Colors](docs/images/font_colors.png)

</details>

The navbar colors are Bootstrap colors, with the exception of the #3B0707, which has been used as the active link color. Unfortunately the Bootstrap included / default color for this kind of navbar, does not pass the contrast test.

<details>
<summary>Navbar Colors</summary>

![Navbar Colors](docs/images/navbar_colors.png)

</details>

The main color-highlight is the animated, gradient background. It contains two base colors and then varies in betweend them.

<details>
<summary>Background Colors</summary>

![Background Colors](docs/images/gradient_base_color.png)
![Background Gradient Colors](docs/images/gradient_45deg_colors.png)

</details>

---

### Typography

[Google Fonts](https://fonts.google.com/) has served to choose Roboto as the main font and Raleway for the main site's title.

<details>
<summary>Fonts</summary>

![Main Font Roboto](docs/images/font_roboto.png)
![Heading Font Raleway](docs/images/font_raleway.png)

</details>

---

### Wireframes

The Wireframes are the prototype of this project and show the base idea and the skeleton of the app. Some details may change during development.

<details>
<summary>Mobile Wireframe</summary>

![Main Site](docs/wireframes/mob/mobile_main.png)
![Sign Up](docs/wireframes/mob/mobile_signup.png)
![Login](docs/wireframes/mob/mobile_login.png)
![Logout](docs/wireframes/mob/mobile_logout.png)
![Collections](docs/wireframes/mob/mobile_collections.png)
![Collection](docs/wireframes/mob/mobile_collection.png)
![Item](docs/wireframes/mob/mobile_item.png)
![Contact](docs/wireframes/mob/mobile_contact.png)
![About](docs/wireframes/mob/mobile_about.png)
![Errors](docs/wireframes/mob/mobile_errors.png)

</details>

<details>
<summary>Desktop Wireframe</summary>

![Main Site](docs/wireframes/dsktp/desktop_main.png)
![Sign Up](docs/wireframes/dsktp/desktop_signup.png)
![Login](docs/wireframes/dsktp/desktop_login.png)
![Logout](docs/wireframes/dsktp/desktop_logout.png)
![Collections](docs/wireframes/dsktp/desktop_collections.png)
![Collection](docs/wireframes/dsktp/desktop_collection.png)
![Item](docs/wireframes/dsktp/desktop_item.png)
![Contact](docs/wireframes/dsktp/desktop_contact.png)
![About](docs/wireframes/dsktp/desktop_about.png)
![Errors](docs/wireframes/dsktp/desktop_errors.png)

</details>

---

### Data Model

The following ERD (Entity Relationship Diagram) displays the SQL database schema and the associated models, used to create this project. It shows the underlaying fundament of the individual models and their relation to it.
Django AllAuth is used to create a user authentication system.

![ERD](docs/images/the_collection_erd_mod.png)

---

## Features


---

### Features Left to Implement

- I had to step back from the idea of having multiple images per item, since this has increased the level of complexity for the whole project quite a lot. Since I have to deliver MVP, I will let this feature for future implementation. I had to adapt the db model to reflect this.

---

## Technologies Used
I used the following technologies and resources to create this site:


---

## Development


---

### Mobile First Approach


---

### Challenges during Development



---

### Commit messages

I have decided to mostly use multiline commit messages. Commit messages are an essential part of the whole project and a single line commit message is just not enough to explain. After reading [this interesting article](https://cbea.ms/git-commit/), it was clear to me, that I have to use it.

I have decided to use (mostly) multiline commits, but using tags as described this [cheatsheet](https://cheatography.com/albelop/cheat-sheets/conventional-commits/) or as also described in the LMS of the Code Institute. I did use the following syntax guidline:
- **feat:** for feature which may or may not include a CSS part
- **fix:** for a bugfix
- **style:** for changes to CSS or to give style to the code itself
- **docs:** for changes related to documentation
- **refactor:** for refactored code, re-written code
- **maint:** for general maintenance

---

## Agile Development Process

### GitHub Projects

### GitHub Issues

### MoSCoW Prioritization

---

## Testing
Testing is covered in a separate page, view [TESTING.md](TESTING.md)


---

## Deployment


---

### Local Deployment

---

## Credits


---

### Code


---

### Content


---

### Media


---

### Acknowledgements


document.addEventListener("DOMContentLoaded", function() {
	const body = document.querySelector(`body`);
	const header = document.querySelector(`header.header`);
	const headerTop = header.querySelector(`.header__top`);
	const headerBottom = header.querySelector(`.header__bottom`);
	const buttonMenu = header.querySelector(`.toggle button`);
	const searchForm = header.querySelector(`.search`);
	const menu = header.querySelector(`.menu--primary`);
	const menuDropdown = header.querySelectorAll(`.menu__item--dropdown`);

	const headerSearch = headerBottom.querySelector(`.search--main`);
	const headerSearchLabel = headerSearch.querySelector(`.label`);

	const toggleMenu = () => {
		const menuSearch = searchForm.cloneNode(true);
		const openedMenu = document.querySelector(`.menu__item--dropdown-opened`) || null;

		buttonMenu.classList.toggle(`button--close`);
		header.classList.toggle(`header--menu-opened`);
		body.classList.toggle(`overflow-hidden`);

		if (header.classList.contains(`header--menu-opened`)) {
			menu.appendChild(menuSearch);
			menu.appendChild(headerTop);
		} else {
			menu.querySelector(`.search`).remove();
			menu.removeChild(headerTop);

			if (openedMenu !== null) {
				openedMenu.classList.remove(`menu__item--dropdown-opened`);
			}
		}
	};

	headerSearchLabel.addEventListener(`click`, (e) => {
		e.preventDefault();
		headerSearch.classList.toggle(`search--active`);
	});

	buttonMenu.addEventListener(`click`, () => toggleMenu());

	menuDropdown.forEach((item) => {
		item.addEventListener(`click`, (e) => {
			e.preventDefault();
			item.classList.toggle(`menu__item--dropdown-opened`);
		});
	});


	// slideshow

	// slideshow images declared in index.html file
	const slideshow = document.querySelector(`.slideshow_images`)

	setTimeout(() => {
		changeImage(slideshow, 'DSC_7097.jpg')
	}, 2000)
});

function changeImage(elem, img_url) {
	elem.src = '/media/' + img_url
}

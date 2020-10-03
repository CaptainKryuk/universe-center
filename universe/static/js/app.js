document.addEventListener("DOMContentLoaded", function() {
	const body = document.querySelector(`body`);
	const header = document.querySelector(`header.header`);
	const headerTop = header.querySelector(`.header__top`);
	const headerBottom = header.querySelector(`.header__bottom`);
	const buttonMenu = header.querySelector(`.toggle button`);
	const searchForm = header.querySelector(`.search`);
	const menu = header.querySelector(`.menu--primary`);
	const menuDropdown = header.querySelectorAll(`.menu__item--phone-dropdown`);

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

	// menuDropdown.forEach((item) => {
	// 	item.addEventListener(`click`, (e) => {
	// 		e.preventDefault();
	// 		item.classList.toggle(`menu__item--dropdown-opened`);
	// 	});
	// });

	// notification
	document.querySelector('.my_toast').addEventListener('click', () => {
		document.querySelector('.my_toast').className = 'my_toast hide_toast'
	})

	setTimeout(() => {
		toast = document.querySelector('.my_toast')
		toast.className = 'my_toast hide_toast'
	}, 3000)


	// slideshow
	if (images) {
		// slideshow images declared in index.html file
		const slideshow = document.querySelector(`.slideshow_image`)

		let i = 0
		a_images = images.split(';')
		let time = 3000

		changeImage(slideshow, i, a_images)

		// reverse slideshow
		const r_slideshow = document.querySelector(`.r_slideshow_image`)
		changeImageReverse(r_slideshow, a_images.length - 1, a_images)
	}

	


});


function changeImage(elem, i, images) {
	elem.src = '/media/' + images[i]

	if (i < images.length - 1) {
		i++
	} else {
		i = 0
	}

	setTimeout(() => {
		changeImage(elem, i, images)
	}, 3000)
}

function changeImageReverse(elem, i, images) {
	elem.src = '/media/' + images[i]

	if (i > 0) {
		i--
	} else {
		i = images.length - 1
	}

	setTimeout(() => {
		changeImageReverse(elem, i, images)
	}, 3000)
}
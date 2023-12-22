document.addEventListener('DOMContentLoaded', function () {
    var ordenDropdown = document.getElementById('ordenDropdown');
    var ordenIcon = document.getElementById('ordenIcon');

    ordenDropdown.addEventListener('click', function (e) {
        if(ordenIcon.classList.contains('fa-angle-down')){
            ordenIcon.classList.remove('fa-angle-down');
            ordenIcon.classList.add('fa-angle-up');
        }else{
            ordenIcon.classList.remove('fa-angle-up');
            ordenIcon.classList.add('fa-angle-down');
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    var ordenDropdown = document.getElementById('ordenDropdown2');
    var ordenIcon = document.getElementById('ordenIcon2');

    ordenDropdown.addEventListener('click', function (e) {
        if(ordenIcon.classList.contains('fa-angle-down')){
            ordenIcon.classList.remove('fa-angle-down');
            ordenIcon.classList.add('fa-angle-up');
        }else{
            ordenIcon.classList.remove('fa-angle-up');
            ordenIcon.classList.add('fa-angle-down');
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    var ordenDropdown = document.getElementById('ordenDropdown3');
    var ordenIcon = document.getElementById('ordenIcon3');
    console.log(ordenDropdown)
    console.log(ordenIcon)

    ordenDropdown.addEventListener('click', function (e) {
        console.log('sdfasdf',e.target)
        if(ordenIcon.classList.contains('fa-angle-down')){
            ordenIcon.classList.remove('fa-angle-down');
            ordenIcon.classList.add('fa-angle-up');
        }else{
            ordenIcon.classList.remove('fa-angle-up');
            ordenIcon.classList.add('fa-angle-down');
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const customOptions = document.querySelectorAll('.custom-options .dropdown-item');

    customOptions.forEach(function (option) {
        option.addEventListener('click', function (event) {
            event.preventDefault();
            const selectedValue = this.getAttribute('data-value');
            document.getElementById('selected_order').value = selectedValue;
            document.getElementById('filterForm').submit();
        });
    });
});

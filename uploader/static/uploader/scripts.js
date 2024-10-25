
document.querySelector('#id_file').addEventListener('change', function () {
    const file = this.files[0];
    const allowedExtensions = ['csv', 'xlsx'];
    const maxSize = 5 * 1024 * 1024; 
    const extension = file.name.split('.').pop().toLowerCase();

    if (!allowedExtensions.includes(extension)) {
        alert('Invalid file type. Only CSV and Excel files are allowed.');
        this.value = ''; 
    } else if (file.size > maxSize) {
        alert('File is too large. Maximum allowed size is 5MB.');
        this.value = ''; 
    }
});


(function () {
    'use strict';
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
})();

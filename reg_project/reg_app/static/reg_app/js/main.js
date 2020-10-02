$(document).ready(function () {
    if ($('#result') != null) {
        Read();
    }
    $('#create').on('click', function (e) {
        $date_responded = $('#date_responded').val();
        $subject = $('#subject').val();
        $sender = $('#sender').val();
        $files = $('#files').val();
        $num_of_file = $('#num_of_file').val();
        $date_of_file = $('#date_of_file').val();
        $date_recived = $('#date_recived').val();

        if ($date_responded == "" || $subject == "" || $sender == "" || $num_of_file == "" || $date_of_file == "" || $date_recived == "") {
            alert("Please complete the required field");
        } else {
            $.ajax({
                url: 'create',
                type: 'POST',
                data: {

                    date_responded: $date_responded,
                    subject: $subject,
                    sender: $sender,
                    files: $files,
                    num_of_file: $num_of_file,
                    date_of_file: $date_of_file,
                    date_recived: $date_recived,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    document.getElementById("main_p").reset();
                }
            });
        }
    });

    $(document).on('click', '.edit', function () {
        $id = $(this).attr('name');
        window.location = "edit_entry/" + $id;
    });

    $('#update').on('click', function () {
        $date_responded = $('#date_responded').val();
        $subject = $('#subject').val();
        $sender = $('#sender').val();
        $files = $('#files').val();
        $num_of_file = $('#num_of_file').val();
        $date_of_file = $('#date_of_file').val();
        $date_recived = $('#date_recived').val();

        if ($date_responded == "" || $subject == "" || $sender == "" || $num_of_file == "" || $date_of_file == "" || $date_recived == "") {
            alert("Please complete the required field");
        } else {
            $id = $(this).attr('name');
            $.ajax({
                url: 'update/' + $id,
                type: 'POST',
                data: {
                    date_responded: $date_responded,
                    subject: $subject,
                    sender: $sender,
                    files: $files,
                    num_of_file: $num_of_file,
                    date_of_file: $date_of_file,
                    date_recived: $date_recived,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    window.location = '/';
                    alert('Updated!');
                }
            });
        }

    });

    $(document).on('click', '.delete', function () {
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete_entry/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                Read();
                alert("Deleted!");
            }
        });
    });

});

function Read() {
    var req = $.ajax({
        url: 'entry',
        type: 'POST',
        async: false,
        data: {
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:
            (response) => {
                $('#result').html(response);

            }
    });

    req.abort()
}
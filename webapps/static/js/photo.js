$(function(){
    $(".a_photo").click(function(){
        var file_path = $(this).data('file-path');
        create_table(file_path);

        $('#modal_thumbnail').modal('show');
    });
});

function create_table(file_path) {
    $("#modal_body_thumbnail").empty();
    $("#modal_body_thumbnail").append("<h5 class='text-center'>Hello. Some text here.</h5>");
    $("#modal_body_thumbnail").append(get_table_body(file_path));
    $("#modal_body_thumbnail").append(get_table_body("1001.jpg"));
    $("#modal_body_thumbnail").append(get_table_body("1002.jpg"));
    $("#modal_body_thumbnail").append(get_table_body("1003.jpg"));
    $("#modal_body_thumbnail").append(get_table_body("1004.jpg"));
}

function get_table_body(file_path) {
    var table_header =
        "<div class='table-responsive'>" +
            "<table class='table table-striped modal_thumbnail_table'>" +
                "<tbody>" +
                    "<tr>";
    var table_footer =
                    "</tr>" +
                "</tbody>" +
            "</table>" +
        "</div>";
    var table_data = get_table_data(file_path)
    return table_header + table_data + table_footer;
}

function get_table_data(file_path) {
    var table_data = ""
    for (var i = 0; i < 10; i++) {
        var img_url = '"/static/photos/' + file_path + '"'
        table_data +=
            "<td class='modal_thumbnail_row'>" +
                "<div class='thumbnail' style='background-image: url(" + img_url + ")'></div>" +
            "</td>";
    }
    return table_data;
}

window.onload = function () {
    let days = document.getElementsByClassName("day")
    for (let i = 0; i < days.length; i++) {
        let day = document.getElementsByClassName("day")[i];
        let time = document.getElementsByClassName("time")[i];
        let title = document.getElementsByClassName("class_title")[i];
        let row_blocks = document.getElementsByClassName("rows");
        let week_days_collection = document.getElementsByClassName("cols")[0].children
        for (week_day in week_days_collection) {
            if (day.innerText == week_days_collection[week_day].innerText) {
                let new_class = week_days_collection[week_day].className;
                title.classList.add(new_class);
            }
        }
        for (let row_block = 0; row_block < row_blocks.length; row_block++) {
            let time_titles = row_blocks[row_block].firstElementChild;
            let time_rows = row_blocks[row_block].children;
            if (time.innerText == time_titles.innerText) {
                for (let time_row = 0; time_row < time_rows.length; time_row++) {
                    let correct_class = time_rows[time_row].className;
                    if (title.classList.contains(correct_class)) {
                        time_rows[time_row].innerHTML = '<h6 class="font-weight-bold">' + title.innerText; + '</h6>'
                    }
                }
            }
        }
    }
}

// '<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal' + class_id.innerText + '">' + 

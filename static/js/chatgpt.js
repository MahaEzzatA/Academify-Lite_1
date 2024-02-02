$(document).ready(function() {
            $('#prompt').val('');
            //Send the form on enter keypress and avoid if shift is pressed
            $('#prompt').keypress(function(event) {
                if (event.keyCode === 13 && !event.shiftKey) {
                    event.preventDefault();
                }
            });

            $('#copied_div').hide();

            $('#form_1').on('submit', function(event) {
                var form =  document.getElementById("form_1");
                // Get the prompt
                var prompt = $('#prompt').val();
                //$('#response').text('');
                // Add the prompt to the response div
                //$('#response').append('<p <i class="bi bi-person"></i>: ' + prompt + '</p>');
                //var selectedTone = "Friendly";
                var selectedTone = document.getElementById("toneSelect").value;

                var copy_icon_source =   "static/img/10310494.png";
                var twitter_icon_source = "static/img/5969020.png";
                var edit_icon_source = "static/img/13488210.png";

                var loading_gif_source = "static/img/loading-yellow.gif";
                var tbl =  document.getElementById("tbl");
                var loading_div =  document.getElementById("loading");

                event.preventDefault();
                // get the CSRF token from the cookie
                var csrftoken = Cookies.get('csrftoken');

                // set the CSRF token in the AJAX headers
                $.ajaxSetup({
                    headers: { 'X-CSRFToken': csrftoken }
                });

                var dateTime = new Date();
                var time = dateTime.toLocaleTimeString();
                while (tbl.hasChildNodes()) {
                    tbl.removeChild(tbl.lastChild);
                }
                //$('#response #GFG1').css({"color": "green", "width": "90%", "float": "left"});
                // Clear the prompt
                //$('#prompt').val('');
                // Show the loading gif
                let loadingIcon = document.createElement('img');
                //$('#response #GFG2').css({"color": "red", "width": "90%", "float": "right"});
                loadingIcon.src = loading_gif_source ;
                //class="u-align-center u-image u-image-contain u-image-default u-preserve-proportions u-image-1"
                loadingIcon.style.display = true;
                //loadingIcon.style.width = "140";  // Set  width
                //loadingIcon.style.height = "177"; // Set height
                loadingIcon.class="u-align-center u-image u-image-contain u-image-default u-preserve-proportions u-image-1";

                $('#loading').append(loadingIcon);
                form_activation(false, form);

                $.ajax({
                    url: '/',
                    type: 'POST',
                    data: {prompt: ' """ '+ prompt + ' """ ' , tone: selectedTone},
                    dataType: 'json',
                    success: function(data) {
                        //$('#tweet').append('<p id="GFG2">('+ time + ') <i class="bi bi-robot"></i>: ' + data.response + '</p>');
                        // Split the returned response to the array
                        const tweetObject = JSON.parse(data.response);
                        array = Object.values(tweetObject);
                        //.split(/\r?\n|\r|\n\d+\-\s+\-\s+/g);
                        //array = data.response.split(/\d+\-\s+/g);
                        //array = data.response.split(/\-\s+/g);
                        if (array.length > 1){
                            for(i in array){
                                array[i] = array[i].replace(/\d+\-/g, '');
                                array[i] = array[i].replace(/\-\s+/g, '');
                                array[i] = array[i].replace(/"/g, '');
                                //Removing emojis if exist
                                array[i] = array[i].replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g,'')
                                //Removing hashtags if exist
                                array[i] = array[i].replace(/\#\w\w+\s?/g, '');
                                if((array[i].length > 0 )&&(array[i].trim().length !== 0)){
                                    build_table_row(tbl,copy_icon_source,twitter_icon_source, edit_icon_source,array[i]);
                                }
                            }
                        }
                        else{
                            array[0] = array[0].replace(/'/g, '');

                            const row = tbl.insertRow();
                            const cell1 = row.insertCell(0);
                            cell1.style.width = '100%';
                            cell1.textContent = array[0];
                        }
                        //$('#response #GFG2').css({"color": "red", "width": "90%", "float": "right"});
                        loading_div.removeChild(loadingIcon);
                        form_activation(true, form);
                        $('#tweet').append(tbl);
                    },
                    error: function( ) {
                        const row = tbl.insertRow();
                        const cell1 = row.insertCell(0);
                        cell1.style.width = '100%';
                        cell1.textContent = "Oops! Something went wrong.\nWe're sorry. Our team has been notified, and we're working to fix the issue. Please try again later!";
                        loading_div.removeChild(loadingIcon);
                        form_activation(true, form);

                        $('#tweet').append(tbl)
                    }
                });//
            });

        });
        //comment comment
        function form_valid() {
            var textareaValue = document.getElementById('prompt').value;
                        var r_btn = document.getElementById("nnn");

            var wordCount = textareaValue.split(/\s+/).filter(function (word) {
                return word.length > 0;
            }).length;

            var wordCountMessage = document.getElementById('wordCountMessage');
            var maxWords = 1000;

            if (wordCount > maxWords) {
                wordCountMessage.textContent = 'Word limit exceeded!';
                r_btn.disabled=true;
                return false;
            } else {
                wordCountMessage.textContent = '';
                r_btn.disabled=false;
                return true;
            }
        }
        // Function to share text on Twitter
        function shareOnTwitter(content) {
            content = content.trim();
            var tweetUrl = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(content);
            window.open(tweetUrl, '_blank');
        }
        // Function to copy text to clipboard
        function copyTextToClipboard(content,btn) {
            navigator.clipboard.writeText(content);
             setTimeout(function ()
            {
                $('#copied_div').fadeIn('slow');
                // Remove the Copied text from the DOM after 2 seconds
                setTimeout(function ()
                {
                    $('#copied_div').fadeOut('slow');
                }, 2000)
            }, 600);
        }
        // Function to toggle the visibility of the dropdown form based on the status
        function form_activation(bool, form) {
            var elements = form.elements;
            for (var i = 0, len = elements.length; i < len; ++i) {
                elements[i].disabled = !bool;
            var reset_btn = document.getElementById("reset_btn");
            reset_btn.disabled =!bool;
            }
        }
        // Function to create table's row:
        function build_table_row(tbl, copy_icon, twitter_icon, edit_icon,post_content) {
            const row = tbl.insertRow();
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            const cell3 = row.insertCell(2);
            const cell4 = row.insertCell(3);

            row.id = "row_" + tbl.rows.length;

            cell1.textContent = post_content;
            create_row_btn(edit_icon, cell2, row, "edit");
            create_row_btn(copy_icon, cell3, row, "copy");
            create_row_btn(twitter_icon, cell4, row, "share");

        }
        // Function to create row's buttons:
        function create_row_btn(icon_source, cell, row, flag) {
            var btn = document.createElement('span');
            btn.innerHTML = "<span class='u-align-center u-border-none u-btn u-button-style u-none u-text-palette-2-base u-btn-2'></span>";
            btn.style = "cursor:pointer;";
            icon = create_icon(icon_source);
            if (flag == "copy") {
                    btn.title = "Copy";
                    btn.addEventListener('click', () => {copyTextToClipboard(row.cells[0].textContent, btn);});
            } else if (flag == "share"){
                    btn.title = "Share on X";
                    btn.addEventListener('click', () => {shareOnTwitter(row.cells[0].textContent);});
            }else{
                    btn.title = "edit";
                    btn.addEventListener('click', () => { openEditPopup(row.cells[0].textContent, btn);});
            }
            btn.append(icon);
            cell.appendChild(btn);
        }
        // Function to create buttons' icons:
        function create_icon(icon_source) {
            let img = document.createElement('img');
            img.src = icon_source;
            img.style.height = '50px';
            img.style.width = '50px';
            return img;
        }
        function reset() {
            $('#prompt').val('');
            $('#toneSelect').val("Friendly");
        }
        function openEditPopup(text, btn) {
            var editText = document.getElementById("editText");
            editText.value = text;

            // Store a reference to the currently edited row in a data attribute
            var row = btn.closest("tr");
            document.getElementById("editPopup").setAttribute("data-edited-row", row.id);

            var editPopup = document.getElementById("editPopup");
            editPopup.style.display = "block";

            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
              if (event.target == editPopup) {
                editPopup.style.display = "none";
              }
            }
        }
        function saveEdit() {
            var editText = document.getElementById("editText");

            // Retrieve the reference to the currently edited row from the data attribute
            var rowId = document.getElementById("editPopup").getAttribute("data-edited-row");
            var selectedRow = document.getElementById(rowId);

            //var selectedRow = document.activeElement.closest("tr");
            selectedRow.cells[0].textContent = editText.value;

            closePopup();
        }

        function closePopup() {
            var editPopup = document.getElementById("editPopup");
            editPopup.style.display = "none";
        }

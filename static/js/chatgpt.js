$(document).ready(function() {
            // Send the form on enter keypress and avoid if shift is pressed
            $('#prompt').keypress(function(event) {
                if (event.keyCode === 13 && !event.shiftKey) {
                    event.preventDefault();
                    $('form').submit();
                }
            });
            var copy_icon_source =   "static/img/1827973.png";
            var twitter_icon_source = "static/img/5969020.png";
            tbl =  document.getElementById("tbl");
            $('form').on('submit', function(event) {
                event.preventDefault();
            // get the CSRF token from the cookie
            var csrftoken = Cookies.get('csrftoken');

            // set the CSRF token in the AJAX headers
            $.ajaxSetup({
                headers: { 'X-CSRFToken': csrftoken }
            });
                // Get the prompt
                var prompt = $('#prompt').val();
                var checkbox = document.getElementById("selectToneCheckbox");
                var loading_div =  document.getElementById("loading");

                var selectedTone = "Friendly";
                if (checkbox.checked) {
                    selectedTone = document.getElementById("toneSelect").value;
                }
                var dateTime = new Date();
                var time = dateTime.toLocaleTimeString();
                $('#response').text('');
                while (tbl.hasChildNodes()) {
                    tbl.removeChild(tbl.lastChild);
                }
                // Add the prompt to the response div
                $('#response').append('<p <i class="bi bi-person"></i>: ' + prompt + '</p>');
                //$('#response #GFG1').css({"color": "green", "width": "90%", "float": "left"});
                // Clear the prompt
                $('#prompt').val('');
                // Show the loading icon
                let loadingIcon = document.createElement('img');
                loadingIcon.src = "static/img/loading-slow-net.gif";

                loadingIcon.style.display = "block";
                //loadingIcon.style.width = "100px";  // Set  width
                //loadingIcon.style.height = "100px"; // Set height

                loadingIcon.style.display = "block";
                //loadingIcon.style.position = "absolute";
                loadingIcon.style.left = "35%";
                loadingIcon.style.top = "35%";
                $('#loading').append(loadingIcon);

                $.ajax({
                    url: '/',
                    type: 'POST',
                    data: {prompt: ' """ '+ prompt + ' """ ' , tone: selectedTone},
                    dataType: 'json',
                    success: function(data) {
                        //$('#tweet').append('<p id="GFG2">('+ time + ') <i class="bi bi-robot"></i>: ' + data.response + '</p>');
                        array = data.response.split(/\r?\n|\r|\n\d+\-/g);
                        if (array.length > 1){
                            for(i in array){
                                array[i] = array[i].replace(/\d+\-/g, '');
                                if((array[i].length > 0 )&&(array[i].trim().length !== 0)){
                                    build_table_row(tbl,copy_icon_source,twitter_icon_source, array[i]);
                                }
                            }
                        }
                        else{
                            const row = tbl.insertRow();
                            const cell1 = row.insertCell(0);
                            cell1.style.width = '100%';
                            cell1.textContent = array[0];
                        }
                        //$('#response #GFG2').css({"color": "red", "width": "90%", "float": "right"});
                        //$('#tweet').removeChild(loadingIcon);
                        loading_div.removeChild(loadingIcon);
                        $('#tweet').append(tbl)
                    },
                    error: function( ) {
                        const row = tbl.insertRow();
                        const cell1 = row.insertCell(0);
                        cell1.style.width = '100%';
                        cell1.textContent = "Oops! Something went wrong.\nWe're sorry. Our team has been notified, and we're working to fix the issue. Please try again later.!";
                        loading_div.removeChild(loadingIcon);

                        $('#tweet').append(tbl)


                    }

                });
            });
        });
        // Function to share text on Twitter
        function shareOnTwitter(content) {
            var tweetUrl = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(content);
            window.open(tweetUrl, '_blank');
        }
        // Function to copy text to clipboard
        function copyTextToClipboard(content) {
            navigator.clipboard.writeText(content);
        }
        // Function to toggle the visibility of the dropdown based on the checkbox state
        function toggleToneDropdown() {
            var checkbox = document.getElementById("selectToneCheckbox");
            var dropdownContainer = document.getElementById("toneDropdownContainer");
            var toneSelect = document.getElementById("toneSelect");
            // toggle the visibility of the dropdown
            dropdownContainer.style.display = checkbox.checked ? "block" : "none";
            if (!checkbox.checked) {
                toneSelect.selectedIndex = 0;
            }
        }
        function build_table_row(tbl, copy_icon, twitter_icon, post_content) {
            const row = tbl.insertRow();
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            const cell3 = row.insertCell(2);

            cell1.textContent = post_content;
            create_row_btn(copy_icon, cell2, post_content, "copy");
            create_row_btn(twitter_icon, cell3, post_content, "share");
        }
        function create_row_btn(icon_source, cell, post_content, flag) {
            var btn = document.createElement('span');
            btn.innerHTML = "<span class='u-border-none u-btn u-button-style u-none u-text-palette-2-base u-btn-2'></span>";
            btn.style = "cursor:pointer;";
            icon = create_icon(icon_source);
            if (flag == "copy") {
                    btn.title = "Copy";
                    btn.addEventListener('click', () => {copyTextToClipboard(post_content);});
            } else {
                    btn.title = "Share on X";
                    btn.addEventListener('click', () => {shareOnTwitter(post_content);});
            }
            btn.append(icon);
            cell.appendChild(btn);
        }
        function create_icon(icon_source) {
            let img = document.createElement('img');
            img.src = icon_source;
            img.style.height = '50px';
            img.style.width = '50px';
            return img;
        }


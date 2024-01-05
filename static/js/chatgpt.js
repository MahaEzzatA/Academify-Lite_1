$(document).ready(function() {


            var form_2 =  document.getElementById("form_2");


            // Send the form on enter keypress and avoid if shift is pressed
            $('#prompt').keypress(function(event) {
                if (event.keyCode === 13 && !event.shiftKey) {
                    event.preventDefault();
                    //$('form').submit();
                }
            });
            form_2.style.visibility = "hidden";

            $('#form_1').on('submit', function(event) {
                    // Get the prompt
                    var prompt = $('#prompt').val();
                    $('#response').text('');
                    // Add the prompt to the response div
                    $('#response').append('<p <i class="bi bi-person"></i>: ' + prompt + '</p>');
                    var selectedTone = "Friendly";
                    submit(event, prompt, selectedTone, "form_1", form_2);
            });
            $('#form_2').on('submit', function(event) {
                var selectedTone = document.getElementById("toneSelect").value;
                var prompt = $('#response').text();
                submit(event, prompt, selectedTone, "form_2", form_2);
            });

        });
        function submit (event, prompt, selectedTone, formId, form){
            var copy_icon_source =   "static/img/1827973.png";
            var twitter_icon_source = "static/img/5969020.png";
            var loading_gif_source = "static/img/loading-slow-net.gif";
            var tbl =  document.getElementById("tbl");
            var loading_div =  document.getElementById("loading");
            //var form = document.getElementById("form_2");


            var copyFeedback = document.createElement("div");
            copyFeedback.id = "copy-feedback";
            copyFeedback.textContent = "Copied to the clipboard";
            copyFeedback.classList.add("hidden");
            copyFeedback.style.color = "green";
            copyFeedback.style.fontWeight = "bold";
            copyFeedback.style.marginTop = "10px";
            copyFeedback.classList.remove("hidden");


            if (formId == "form_1"){
                toggleToneDropdown(false, form, false);
            }
            else
                toggleToneDropdown(true,form,false);

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
            $('#prompt').val('');
            // Show the loading gif
            let loadingIcon = document.createElement('img');
            loadingIcon.src = loading_gif_source ;
            //class="u-align-center u-image u-image-contain u-image-default u-preserve-proportions u-image-1"
            loadingIcon.style.display = true;
            //loadingIcon.style.width = "100px";  // Set  width
            //loadingIcon.style.height = "100px"; // Set height
            loadingIcon.className="u-align-center u-image u-image-contain u-image-default u-preserve-proportions u-image-1";

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
                    array = data.response.split(/\r?\n|\r|\n/g);
                    array = data.response.split(/\d+\-\s+/g);
                    if (array.length > 1){
                        for(i in array){
                            array[i] = array[i].replace(/\d+\-/g, '');
                            if((array[i].length > 0 )&&(array[i].trim().length !== 0)){
                                build_table_row(tbl,copy_icon_source,twitter_icon_source, array[i]);
                            }
                        }
                        toggleToneDropdown(true, form, true);
                    }
                    else{
                        toggleToneDropdown(false, form, false);
                        const row = tbl.insertRow();
                        const cell1 = row.insertCell(0);
                        cell1.style.width = '100%';
                        cell1.textContent = array[0];
                    }
                    //$('#response #GFG2').css({"color": "red", "width": "90%", "float": "right"});
                    loading_div.removeChild(loadingIcon);
                    $('#tweet').append(tbl);
                },
                error: function( ) {
                    const row = tbl.insertRow();
                    const cell1 = row.insertCell(0);
                    cell1.style.width = '100%';
                    cell1.textContent = "Oops! Something went wrong.\nWe're sorry. Our team has been notified, and we're working to fix the issue. Please try again later!";
                    loading_div.removeChild(loadingIcon);
                    $('#tweet').append(tbl)
                }

            });
            //
        }
        // Function to share text on Twitter
        function shareOnTwitter(content) {
            content = content.trim();
            var tweetUrl = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(content);
            window.open(tweetUrl, '_blank');
        }
        // Function to copy text to clipboard
        function copyTextToClipboard(content,btn) {
            navigator.clipboard.writeText(content).then(function() {
                // Set the tooltip text
                btn.setAttribute("title", "Text copied to clipboard");

                // Reset the tooltip after a delay (e.g., 2 seconds)
                setTimeout(function() {
                    btn.removeAttribute("title");
                }, 2000);
            });
        }
        // Function to toggle the visibility of the dropdown form based on the status
        function toggleToneDropdown(bool, form, status) {
            var toneSelect = document.getElementById("toneSelect");
            if(bool){
                form.style.visibility = "visible";
                var elements = form.elements;
                for (var i = 0, len = elements.length; i < len; ++i) {
                    elements[i].disabled = !status;
                }
            }
            else{
                form.style.visibility = "hidden";
                toneSelect.selectedIndex = 0;
            }
        }
        // Function to create table's row:
        function build_table_row(tbl, copy_icon, twitter_icon, post_content) {
            const row = tbl.insertRow();
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            const cell3 = row.insertCell(2);

            cell1.textContent = post_content;
            create_row_btn(copy_icon, cell2, post_content, "copy");
            create_row_btn(twitter_icon, cell3, post_content, "share");
        }
        // Function to create row's buttons:
        function create_row_btn(icon_source, cell, post_content, flag) {
            var btn = document.createElement('span');
            btn.innerHTML = "<span class='u-border-none u-btn u-button-style u-none u-text-palette-2-base u-btn-2'></span>";
            btn.style = "cursor:pointer;";
            icon = create_icon(icon_source);
            if (flag == "copy") {
                    btn.title = "Copy";
                    btn.addEventListener('click', () => {copyTextToClipboard(post_content, btn);});
            } else {
                    btn.title = "Share on X";
                    btn.addEventListener('click', () => {shareOnTwitter(post_content);});
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


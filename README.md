Young Alumni Museum Exhibit
Summer 2018


Courtney Solano, Erin Ruby, Kara Metcalfe




**Database**

The database we used is MongoDB Atlas. It is a cloud based database. We used GridFS to store the photos in the database, which are broken up into two collections, fs.files and fs.chunks. The rest of the data is stored in the people collection. All three collections are within the prototype database. The attributes for each entry include a name, subtitle, heading, icon, image1, paragraph1, image2, paragraph2, image3, paragraph3, category, and hidden. The hidden attribute is used to hide entries on the display page. We used PyMongo to work with the database. It is a Python distribution that contains tools to work with MongoDB. It has many built-in functions to add, retrieve and edit entries in the database.
In the future, a second hidden attribute will be added to so an entry can be hidden from the display page but still be searchable or found from the index, as opposed to being hidden from everything.  As more and more entries get added, it might be a good idea to create separate collections for each of the main tabs. It would create better organization when trying to retrieve entries.
Another idea for the future is to have the database stored both in the cloud and locally on a raspberry pi. This way, the information will be quickly accessible but also up to date. The raspberry pi would occasionally pull the information from the database, most likely at a low traffic time, and store it locally. Then the application would not need to access the internet every time a user tries to access information.

 
 
 
**Add Entry, Edit, and Search Functions**

*Add Entry*

The Add Entry function is called hello in the new_entry_form python file. It consists of a form that has inputs for all of the dynamic content on the site, such as names, subtitles, paragraphs, and images of content shown on the display. When a user submits this form, the information is grabbed from the form and sent to the database through the addOne function, in the add_person python file.
In the addOne function, the parameters that are passed through correspond to the attributes in the database. They are stored into a dictionary, then passed to a built-in PyMongo function called insert_one. The function takes in the list of information that has been inputted by the user and cleaned by the hello function, and puts it all into the database. It first establishes a connection to the database using a name and password. Then, the raw images are taken from the /static/imj folder and stored into the database. This was initially done so we could dynamically retrieve images from the database instead of storing them all in a folder, especially when the number of entries becomes too large for the raspberry pi to store. However, we were not able to get this feature to work properly with the display, so this is something that would be beneficial to implement in the future.
After the photos are stored, the information is stored as "key, value" pairs in a dictionary. This means that every piece of information has a unique identifier that can be used to look up that value in the database. This block of information is then inserted into the database using the built in insert_one function from PyMongo. If the information is successfully added, the terminal will print out a statement saying that piece of content was added.
When cleaning the information to send to the database, all of the plain text information does not need any special treatment, but the images and checkboxes do if they do not have information stored. If an image is not uploaded, the form will not submit, so a default image is provided. Similarly, if a checkbox is checked, a "1" will be stored, but if the checkbox is not checked, the input will be blank and the form will not submit. The checkbox function handles this, storing a "0".
To improve the Add Person function, we would like to have some form validation, so a user cannot upload an image that is too large, or possibly inject malicious code through our text inputs. Also, currently it is required that a user uploads three photos, which could be a problem if the user only has two photos, or there is not enough content to show three photos with text. The curators suggested that this was a positive thing, because it challenges them to come up with thorough details about content they are inputting. But there might be times where a user just wants to upload one photo for a entry. Therefore, this should be a possible feature. It might be nice to have required fields so, for example, a user must have a title for each page. Lastly, it is important to add a page after a user inputs content that says the upload was successful. Currently we have a print statement in the code, but users are not able to see this on the front end.

*Edit Entry*

The Edit function is set up in a similar manner to the Add Person function. The key difference between the two is that the Edit function grabs the data for the person (or building, or artifact) from the database and pre-populates the information into the form, so a user knows what is currently stored. To change the information, the user will retype the new information into the corresponding field of the form and press submit. The old information is overwritten. This functionality works for all fields except the photo field, which is something that the curators would greatly benefit from having. The information is grabbed from the form and passed into the database through the editOne function in the edit_person python file. This is another thing that can be improved, because it would be nice to have the old information stored somewhere so an "undo" would be possible if edits were made in error.
The editOne function is similar to the addOne function, one difference being the built-in PyMongo function that is called. The function also requires the ID attribute of the entry that is being edited. This is required because we aren't making a new entry into the database, just updating an existing one. This function makes it simple to edit a specific set of information by passing in the user's ID as the first argument, and "$set" along with the entry's updated information as the second argument. A connection to the database is established, the updated images are uploaded to the database, and the edited information is stored as "key, value" pairs.
One major improvement to the Edit function would be having an "Edit Successful" page that a user is sent to once a change is successfully made. Currently there is a print statement in the python code, but the user is not able to see this on the front end of the application. Similar to the Add One function, all images are required to submit but are not being pre-populated, so every time an edit is made, the user has to upload the pictures again. This is a major flaw and it would greatly benefit the curators to allow image fields to be left blank and have the images from the database already be on the edit page.

*Search*

The search functions are all located in the retrieve_from_db python file. Each function uses the same built-in PyMongo function find_one, but are all used for searching for different things. The search page allows the user to click on a letter, then it will return all entries in the database that begin with that letter. In the future, it would be helpful to also return people who have a last name that begins with that letter as well. The display page calls a function that will return all entries from that category and store it individual arrays. The display page html knows which category the user clicks, so it displays all entries that are in the array. It would be quicker to have the user click the category first, then pull from the database, rather than preloading all the categories. It works now because there are not many things in the database. The search page is intended to be used only by the museum curators and not by the general public.
The index page is how the public can search for entries. It is accessible from the display page and shows the names of everything stored in the database. It is sorted in alphabetical order. The curators want the index page to look like the other display pages. Like the search page, it will be good to have the alphabet list somewhere on the index to narrow it down. The index should also be scrollable.




**Display Page Info Organization**

There are a series of arrays holding a hierarchy of information throughout the site. The top of this hierarchy is the three tabs- people, history and athletics. An array of tabs holds all the different tabs. There are three tabs in this array. Adding more things to this array will allow more tabs to be added on additional screens (e.g. a science, news, and artifacts tab on another screen). The tabs are always present on the bottom of the site and link to a "home page" for the pressed tab. Pressing the "people" tab links to a people "home page".
Each of the tabs hold an array of categories. For example, the "people" array holds astronauts, early faculty and athletes. The "history" array holds timeline, buildings, and facts. These categories will be available in the sliding bar on the corresponding home page. The people home page has a sliding bar with astronauts, early faculty and athletes. Clicking one of these in the scroll bar will link you to another home page, e.g. clicking "athletes" will link you to an athletes home page. The athletes home page has a scroll bar populated with members of the "athletes" array, such as Emma Coburn, Byron White and David Bolen. Clicking on one of these people in the scrollbar will not link to another page, but present info on the person clicked.
Below is a picture to show the structure more clearly. Currently, not all arrays have much in them, but expansion and adding array members to the database should be simple. The array in which entries are added correspond to the category attribute in the database.




**General Layout**

Each page on the site has a large picture covering the entire top of the screen. There is a "heading" and possible subheading in a black area below this, with text in a grey, curved area below the heading. The text will overflow out of this area if the paragraph is too long, so it is important to make sure there are not too many words in the text area. Below this is a horizontal scrollbar with scrolling arrows, it depicts members of a certain array. Below this is a tab section, currently holding "people, history and athletics" tabs.
The container, forAbout and about divs hold everything above the scrollbar. In the about div, a tabContent div exists where information (picture, heading, subheading and paragraph) on each member of the current array is pulled from the database (the entire array loads on the page at once). For example, on the athletes page, Emma Coburn will load at once.
The buttons div holds the arrows and scrollbar. There are links to javascript to help the scrollbar work. Below this are the tabs in the categories div. There are also two curved graphics (top one grey, bottom one black) overlapping the page. The grey one gives a curve to the information section, while the second makes a curve while tapping on the tabs and makes the tabs look a bit more exciting.

*Important*- the exact size of the viewing screen is unknown. Many things, including the large topmost image and curve graphics must be resized to fit the exact size of the screen when it is known. It can be assumed that the entire display will need to be made to be more vertical. Set the display to 560px width to see what it looks like now.




**Photos and Photo Content**

The photos are all located in YAME/form_ui/static/img. This includes simple graphics such as the curves for the pages as well as the main images for every array category. Currently, every image that will go in the topmost part of the screen must be 2400 x 1920 for the layout to work. The pictures in the scrollbar also must be of the same ratio as the top images.
Many images have 4 variants of the same picture/name, e.g. name_icon, name_image1, name_image2, and name_image3. The first variant, name_icon, includes text and is placed in a scrollbar for the user to see and tap on for more information. The font in the image is part of the picture, use (https://drive.google.com/open?id=1cdqyR8Wlqj10g8_R2CWAgZ94QjiokstP ) to access forMakingImageText.psd, the photoshop file for making images with font in the correct place.
The other three variants are for use as large, top images. The three images and their descriptions can be scrolled through. For example, Football_image1, Football_image2, and Football_image3 will be up at the top of the page to scroll through when a user selects "Football" in the scrollbar.
Some images in here, such as glenn_asakawa, are unused. These can be used in the future as new entries are created in the database.
The font in the icon images and throughout the site is Helvetica Neue. There is a fonts folder holding different variations of this font; make sure they are installed on the viewing device, as the site will not look right otherwise. The font in the icon images specifically is Helvetica Neue Condensed Black; use this to edit the text in these images.




**Future Plans**

Debug- the main thing here is the loading time. It takes around five seconds for each tab to load, as well as each category in the tabs. We would love to add some code that makes this an instantaneous process.

Improve- The arrays holding tabs, categories and subcategories could use improvement. Currently, the arrays are hard coded in to the HTML and python code for the display in order to create the structure of the application that we currently are using. In the future, it is crucial to the expansion of the project that this code becomes generalized, because if a user wants to add a new category, they have to go into both code files and add the new array, populate it, return that array, and utilize it in the HTML.
The same idea applies for the add person page, specifically for the category dropdown menu. If a user wants to add a new category, they have to go into the HTML and manually add an option for a new array. It would be great if the category names were generally added to that dropdown when a user inputs a new category, so it is possible to add new content under that category.
Our search function needs improvement so that a user might find more accurate results when searching. Right now, searching only provides results based on first names/first words of a search. Searching for things that start with "C" would bring up Christopher Bell, but Emma Coburn would not be mentioned, since the C in her name is in the second word.
Users also should be able to search by more than just a letter in the future. They might search for year graduated, an industry, a product, a discovery, etc. The search would need to be flexible. For example, searching for year graduated 2005 would need to return those who graduated from CU in 2005 first, and then display those who graduated in 2006 or 2004, etc. with the most visible results being closest to 2005.
The letters in the search (as well as future categories) might be organized into scrollbars like the scrollbar on the display pages for ease of use.
It may be decided that the search can be replaced by the index with everything a user could find in the database, from an artifact to a building to an old Ralphie. The current index needs improvement. The layout needs to match the rest of the display. We would suggest something like the picture below, with a scrollbar for the user to select the first letter of what they are looking for, then the index jumps to the correct location.  

The add/edit entries function needs some work. Right now, three images must be added to be able to submit the forms, and for the top screen image scroll to work. We would like this to be dynamic. If no picture was added by a curator, a default image will be added to the database and thus shown on the display. If you edit anything in the database and do not reupload the pictures, the edit will also not work.

Add- Adding "back buttons" on pages would improve user experience. On the display, once an item is clicked there is not a back button to exit from the content back to the main category page (For example, if you click on Emma Coburn in the Athletes category, there is no way to get back to the main Athletes page). This would be a feature that would not be extremely difficult to include, but would be helpful for users to navigate the application.
Also on the display, it would be beneficial for users to see which main tab (People, Buildings, Athletics) they are under. By adding a gold color to the tab they are currently on, it would enhance their experience and make navigation through the application easier to understand. See the picture below, if someone was looking at information under the "people" tab.


In the further future, it would be great to add dynamic sizing for the project. Right now, it only looks good at a very specific width, and it would be great for online users to be able to access the project on an alumni or museum site and have it look great on any sized screen.
Adding survey capabilities would help the curators know which information in the database is most popular. If there was something to track the number of times people tap on "astronauts" in the scroll bar, curators would know how popular this item is. If the number of times people press "search" is tracked, curators would know how popular searching is over finding something through the scrollbars and tabs. Knowing this data, the curators and future project developers will know how to move forward.

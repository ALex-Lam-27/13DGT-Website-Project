const destinations = {

    library: {

        name: "Library",

        directions: [

            "Start at the Main Entrance beside Mackillop Campus.",

            "Walk straight towards Administration.",

            "Continue past Student Reception.",

            "Walk past the Careers Hub.",

            "Continue until you reach the Library."

        ]

    },

    science: {

        name: "Science Faculty",

        directions: [

            "Start at the Main Entrance.",

            "Walk straight towards Administration.",

            "Continue along the main pathway.",

            "The Science Faculty is beside the L Block classrooms."

        ]

    },

    careers: {

        name: "Careers Hub",

        directions: [

            "Start at the Main Entrance.",

            "Walk towards Administration.",

            "Continue straight ahead.",

            "The Careers Hub is beside Student Reception."

        ]

    },

    gym: {

        name: "Gymnasium / Hall",

        directions: [

            "Start at the Main Entrance.",

            "Walk left along the main pathway.",

            "Continue past the Whare.",

            "The Gymnasium / Hall is beside the sports field."

        ]

    },

    canteen: {

        name: "Canteen",

        directions: [

            "Start at the Main Entrance.",

            "Walk towards Administration.",

            "The Canteen is beside Student Reception."

        ]

    },

    admin: {

        name: "Administration / Reception",

        directions: [

            "Walk straight from the Main Entrance.",

            "Administration / Reception is directly in front of you."

        ]

    },

    international: {

        name: "International Office",

        directions: [

            "Start at the Main Entrance.",

            "Walk towards the left side of campus.",

            "Continue until you reach INT 1 and INT 2.",

            "The International Office is located there."

        ]

    },

    study: {

        name: "C19 Study Room",

        directions: [

            "Start at the Main Entrance.",

            "Walk towards Administration.",

            "Continue to C Block.",

            "The C19 Study Room is inside C Block."

        ]

    },

    whare: {

        name: "Whare",

        directions: [

            "Start at the Main Entrance.",

            "Walk left.",

            "Continue until you reach the Whare."

        ]

    },

    nblock: {

        name: "N Block",

        directions: [

            "Start at the Main Entrance.",

            "Walk towards Administration.",

            "Continue along the main pathway.",

            "Walk past the Library.",

            "N Block is at the far right side of campus."

        ]

    }

};



// GET DIRECTIONS BUTTON

function showDirections() {

    const selected = document.getElementById("destinationSelect").value;

    if (selected === "") {

        alert("Please select a destination.");
        return;
    }

    displayDirections(selected);

}


// DISPLAY DIRECTIONS

function displayDirections(place) {

    const data = destinations[place];

    document.getElementById("directionTitle").textContent =
        "Directions to " + data.name;

    const list =
        document.getElementById("directionsList");

    list.innerHTML = "";

    data.directions.forEach(step => {

        const li = document.createElement("li");

        li.textContent = step;

        list.appendChild(li);

    });

}


// POPULAR PLACES BUTTONS

function quickSelect(place) {
    document.getElementById("destinationSelect").value = place;
    displayDirections(place);
}


// PAGE LOAD

window.onload = function () {
    document.getElementById("searchInput").value = "";
};
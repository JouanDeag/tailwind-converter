if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

        colors = []
        color = []

        for i in range(len(lines)):
            if lines[i] == "50":
                color.append(lines[i])
            elif lines[i] == "900":
                # Add the last element to the list
                color.append(lines[i])
                color.append(lines[i + 1])

                # Delte the first element of the list if it starts with #
                if color[0].startswith("#"):
                    color.pop(0)

                # Group each pair of color and number into a single element
                for i in range(1, len(color) - 1):
                    color[i : i + 2] = [" ".join(color[i : i + 2])]

                # Remove the empty elements at the end of the list
                while color[-1] == "":
                    color.pop()

                # Prepare for next color by adding the list to the colors list
                colors.append(color)
                color = []
            else:
                # Add the color name to the list
                color.append(lines[i])

        # Add the starting bracket to the css string
        css = ":root {"

        # Format into css variables
        for color in colors:
            for hue in color:

                # Split the string into a list
                hue = hue.split(" ")

                # Check if the list has more than one element (not the color name)
                if len(hue) > 1:
                    # Add the color variable to the css string
                    css += f"  --color-{color[0].lower()}-{hue[0]}: {hue[1]};\n"
                else:
                    # Add the color name as a comment
                    css += f"\n  /* {color[0]} */\n"

        # Add the ending bracket to the css string
        css += "}"

        # Write to file
        with open("output.css", "w") as f:
            f.write(css)

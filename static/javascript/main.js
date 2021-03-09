function imageConverter() {
    return {
        imageUrl: "",
        imageName: "",

        fileChosen(event) {
            this.fileToDataUrl(event, (src, name) => {
                this.imageUrl = src
                this.imageName = name
            })
        },

        fileToDataUrl(event, callback) {
            if (!event.target.files.length) return

            let file = event.target.files[0],
                reader = new FileReader()

            reader.readAsDataURL(file)
            reader.onload = e => callback(e.target.result, file.name)
        },
    }
}

function responsiveText() {
    return {
        onLoad: function () {
            var element = this.$refs.text
            var w = element.scrollWidth;
            var h = element.scrollHeight;
            this.$refs.svg.setAttribute("viewBox", "0 0 " + w + " " + h);
        }
    }
}

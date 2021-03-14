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
        },

        copyText: function () {
            var copyText = this.$refs.text.textContent;
            var fullLink = document.createElement('textarea');

            document.body.appendChild(fullLink);

            fullLink.value = copyText;
            fullLink.select();

            document.execCommand("copy", false);

            fullLink.remove();

            this.$refs.copyButton.textContent = "Copied to Clipboard!"
        },

        saveImg: function () {
            var pre = document.createElement('pre');

            pre.style.backgroundColor = this.$refs.container.style.backgroundColor
            pre.style.color = this.$refs.text.style.color
            pre.style.display = "static"
            pre.style.width = "fit-content"
            pre.style.fontWeight = 700
            pre.style.lineHeight = "18px"

            pre.textContent = this.$refs.text.textContent

            document.body.appendChild(pre);

            domtoimage.toPng(pre)
                .then(function (dataUrl) {
                    var img = new Image();
                    img.src = dataUrl;

                    var link = document.createElement("a");
                    link.download = 'banner.png';
                    link.href = dataUrl;
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    delete link;

                })
                .catch(function (error) {
                    console.error('oops, something went wrong!', error);
                    pre.remove();
                });
        }
    }
}

import QtQuick
import QtQuick.Controls

ApplicationWindow {
	visible: true
	width: 500
	height: 400
	font.pixelSize: 40

	Text {
		text: 'Batatinha'
	}

	Button {
		text: 'Botão'
		width: 200
		height: 100
		anchors.horizontalCenter: parent.horizontalCenter
		anchors.verticalCenter: parent.verticalCenter
	}
}

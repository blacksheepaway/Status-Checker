# Website Status Checker

Welcome to the Website Status Checker project! This application helps users monitor the status of a given website by periodically checking the server's HTTP response code. Users can also manually check the website status with a single click. The application uses a simple and clean GUI built with `PySimpleGUI`, making it easy for users to interact with and understand the server status.

## How it Works

The Website Status Checker application allows users to input a URL to monitor. Users can then either manually check the website status by clicking the "Check Now" button or set up a periodic check with a specified time interval. The application sends an HTTP request to the server using the `requests` library and then processes the response code to determine the server status. The status is then displayed in a popup window.

## Technologies and Techniques

- Python
- HTTP status checking with `requests`
- Threading for periodic status checks
- `PySimpleGUI` for creating the graphical user interface

## Example

When the Website Status Checker application is run, users can input the URL they want to monitor. After clicking "Check Now" or setting a periodic check, the application fetches the server status and displays it in a popup window.

<p align="center">
  <img src="https://user-images.githubusercontent.com/50200471/230754162-50cfa742-94c8-48b5-beb9-078f5b7f7c8c.png" width="350" title="hover text">
  <img src="https://user-images.githubusercontent.com/50200471/230754175-88a080bd-6cbb-4b05-9e61-452ecc0feb51.png" width="350" alt="accessibility text">
</p>

## Modification for Other Applications

The Website Status Checker application can be easily modified for various purposes. For example, you could:

- Add more detailed information about the server status, such as server response time and latency
- Create a dashboard to monitor multiple websites simultaneously
- Integrate with a notification system to send alerts when a server's status changes

## Contribution

Contributions to improve or expand the project are highly appreciated. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add a new feature'`)
4. Push your branch to your fork (`git push origin feature-branch`)
5. Create a pull request

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify, and distribute the code as long as the license terms are met.

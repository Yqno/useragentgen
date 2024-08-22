from fake_useragent import UserAgent

# Create a UserAgent instance
ua = UserAgent()

# Ask the user if they want a specific or random User-Agent
choice = input("Would you like a specific User-Agent or a random one? (Enter 'specific' or 'random'): ").strip().lower()

if choice == 'specific':
    # Specific OS, browser, and WebKit options
    os_choice = input("Choose your OS (windows, linux, mac): ").strip().lower()
    browser_choice = input("Choose your browser (chrome, firefox, safari): ").strip().lower()

    if os_choice == 'windows':
        os = ua.windows
    elif os_choice == 'linux':
        os = ua.linux
    elif os_choice == 'mac':
        os = ua.macos
    else:
        print("Invalid OS choice, defaulting to random.")
        os = ua.platform

    if browser_choice == 'chrome':
        browser = ua.chrome
    elif browser_choice == 'firefox':
        browser = ua.firefox
    elif browser_choice == 'safari':
        browser = ua.safari
    else:
        print("Invalid browser choice, defaulting to random.")
        browser = ua.browser

    # In this case, we do not separately choose WebKit; it's included in the generated browser string
    user_agent = f"Mozilla/5.0 ({os}) {browser}"

elif choice == 'random':
    # Randomly generate the entire User-Agent
    user_agent = ua.random

else:
    # Handle invalid input by defaulting to a random User-Agent
    print("Invalid choice, generating a random User-Agent.")
    user_agent = ua.random

# Output the User-Agent string
print("Generated User-Agent:", user_agent)


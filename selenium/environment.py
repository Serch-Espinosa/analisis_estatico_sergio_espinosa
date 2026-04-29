def after_scenario(context, scenario):
    """Close the browser after each scenario."""
    if hasattr(context, "driver"):
        context.driver.quit()

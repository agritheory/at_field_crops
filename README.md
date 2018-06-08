## Deprecated
Similar features are now available in the core of ERPNext. Please use that module instead. This is now left here for posterity.

## Field Crops

This module for ERPNext is designed to work for a small farmer raising crops. A livestock module is available separately.

## Terminology

The doctypes included here and their intended uses are:

* **Acerage**: Used in the case as a synonym to 'field', 'cropland', 'vineyard' or 'orchard', used to represent a an area where crops are grown. Because `fields` is effectively a reserved word in ERPNext referring to form and/or input fields, I have opted to call what a farmer would normally refer to as 'fields' as the less ambiguous 'acreage' instead, even though it isn't a common expression.

* **Crop Variety**: A reuseable doctype for defining key variables about a species and variety, "Silver Queen Sweet Corn" for example.

* **Planting**: Planting is an instance of a Crop Variety, a specific example would be a planting of "Silver Queen Sweet Corn" on 6/1/17. Multiple plantings can exist for Crop Variety and the can occur in the same or different acreages.

* **Harvest**: This doctype references a planting, asks the user to input a yield and moves the result to Stock.

* **Fieldwork**: This allows a crop-specific task to be assign to a user.

## Quickstart

To begin using, first create an acreage, a crop variety and then a planting. You can then assign tasks in fieldwork or harvest a crop.

## A Video Demonstration


## Context

I have been working on an implementation for farmers in ERPNext for about a year and a half. I became confident that I had something really good and that I could build a consulting business around it as an Open Source project. I’m recorded a video preview of my application, embedded below.

My design decisions were informed by my real world experiences as I have spent my entire career in agricultural services (minus a recent detour to electronics manufacturing), including working as a lender and consultant at one of the largest agricultural cooperative banks in the US and by far the largest in my region. I was controller of a large farm (100 FTEs, 900 acres, two locations, 100% directly marketed to retail customers through two farm stands), and I briefly was an insurance agent focusing of farm property insurance. I’ve been consulting with farmers on systems and profitability for 10 years. The point of this is to say that I’ve designed these applications to fit the problems I faced and that I saw my customers facing. Your customers’ problems will likely be different and may not be well reflected in this app. That’s OK. I’m not trying to proscribe the right way to do this, I’m taking a design position based on my experience. That experience is based in northeast United States, where farms are dominated by wholesale dairies and diversified, vertically integrated farms that do things like grass-fed beef, dairy-cow-to-retail-ice-cream and CSAs of all kind of variations.

## Further Enhancements

I have several goals for the next version of this app.

* **Aerial Photos/ Map Integration**: I'd like to incorporate a mapping functionality and add it to the "Acreage" doctype. Ideally, this would have multiple pins that could be used to calculate area, which should be captured in its own docfield. A further enhancement would be to integrate it with an infrared satellite photography service link [Cornerstone Mapping](http://cornerstonemapping.com/precision-ag-thermal-infrared/) or [TerrAvion](https://www.terravion.com/) or others as appropriate, though these are typically a subscription service.

* **Weather Integration**: I am a particular fan of tracking degree days for crops and would love to integrate it further here and have done some of the preliminary work to do so. I would like to find a weather service that doesn't require an API key but I'm not sure it exists. Also, it would be great to integrate it with any of the off-the-shelf hardware weather stations that are on the market.

#### License

GNU AGPLv3

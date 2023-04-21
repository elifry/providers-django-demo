import React from "react";

export default class Badge extends React.Component {
  render() {
    return (
      <>
        <div className="relative pt-1">
          <div className="flex mb-2 items-center justify-between">
            <div>
              <span className="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200">
                Task in progress
              </span>
            </div>
            <div className="text-right">
              <span className="text-xs font-semibold inline-block text-lightBlue-600">
                0%
              </span>
            </div>
          </div>
          <div className="overflow-hidden h-2 mb-4 text-xs flex rounded bg-lightBlue-200"></div>
        </div>
      </>
    );
  }
}
